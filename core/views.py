import urllib
import time

from core.models import User, Present, Birthday, BirthdayContribution
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from core.forms import get_validation_errors, UserRegisterForm
from core.utilities import build_response, prepare_response, get_domain, get_facebook_friends
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.template import RequestContext, loader
from bs4 import BeautifulSoup

def facebook_login(request):
    # TODO: Add CSRF prevention
    login_link = 'https://www.facebook.com/dialog/oauth?' + urllib.urlencode(
        {
            'client_id': settings.FACEBOOK_APP_ID,
            'redirect_uri': get_domain(request) + '/',
            'response_type': 'code',
            'scope': 'email,user_birthday,friends_birthday',
        }
    )
    return HttpResponseRedirect(login_link)

def signout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def api_user_register(request):
    benchmark_start = time.time()
    response = prepare_response(request)
    status = 200
    form = UserRegisterForm(request.POST)
    errors = get_validation_errors(form)
    if form.is_valid():
        data = form.cleaned_data
        new_user = User(email=data['email'])
        new_user.set_password(data['password'])
        new_user.save()
        response['new_user_id'] = new_user.id
        status = 201
    else:
        response['errors'] = errors
        status = 400
    response['meta']['status'] = status
    benchmark_end = time.time()
    response['meta']['execution_time'] = benchmark_end - benchmark_start
    return build_response(response, status=status)

@csrf_exempt
@login_required
def api_present_parse(request):
    benchmark_start = time.time()
    response = prepare_response(request)
    status = 200
    try:
        item_link = request.POST['item_link']
        response['item_link'] = item_link
        conn = urllib.urlopen(item_link)
        page_response = conn.read()
        conn.close()
        soup = BeautifulSoup(page_response)
        asn = soup.find('input', {'id': 'ASIN'})['value']
        response['asn'] = asn
        try:
            birthday_id = request.POST['birthday_id']
            birthday = Birthday.objects.get(id=birthday_id)
            response['birthday_id'] = birthday_id
        except Birthday.DoesNotExist:
            birthday = None
        if birthday:
            try:
                present = Present.objects.get(asn=asn, birthday=birthday)
                status = 204
            except Present.DoesNotExist:
                name = soup.find('span', {'id': 'btAsinTitle'}).find(text=True)
                response['name'] = name
                try:
                    image_link = soup.find('img', {'id': 'original-main-image'})['src']
                except:
                    try:
                        image_link = soup.find('img', {'id': 'main-image'})['src']
                    except:
                        image_link = None
                response['image_link'] = image_link
                cost = float(soup.find('span', {'id': 'actualPriceValue'}).find(class_='priceLarge').find(text=True).split('$')[1])
                response['cost'] = cost
                new_present = Present()
                new_present.item_link = item_link
                new_present.image_link = image_link
                new_present.name = name
                new_present.cost = cost
                new_present.asn = asn
                new_present.birthday = birthday
                new_present.save()
                birthday.amount_target += cost
                birthday.save()
                status = 201
        else:
            status = 404
    except KeyError:
        status = 400
    response['meta']['status'] = status
    benchmark_end = time.time()
    response['meta']['execution_time'] = benchmark_end - benchmark_start
    return build_response(response, status=status)

@csrf_exempt
@login_required
def api_friend_list(request):
    benchmark_start = time.time()
    response = prepare_response(request)
    status = 200
    try:
        friend_list =  get_facebook_friends(request)['data']
        response['friend_list'] = friend_list
    except:
        status = 400
    response['meta']['status'] = status
    benchmark_end = time.time()
    response['meta']['execution_time'] = benchmark_end - benchmark_start
    return build_response(response, status=status)

@csrf_exempt
@login_required
def api_birthday_join(request):
    benchmark_start = time.time()
    response = prepare_response(request)
    status = 200
    birthday_id = request.POST['birthday_id']
    if birthday_id:
        try:
            birthday = Birthday.objects.get(id=birthday_id)
            response['birthday_id'] = birthday_id
            contribution = BirthdayContribution()
            contribution.birthday = birthday
            contribution.contributor = request.user
            contribution.save()
            response['birthday_contribution_id'] = contribution.id
            status = 201
        except Birthday.DoesNotExist:
            status = 404
    else:
        facebook_id = request.POST['facebook_id']
        birthday_date = request.POST['birthday']
        birthday = Birthday(facebook_id=facebook_id, birthday=birthday_date)
        birthday.save()
        response['birthday_id'] = birthday.id
        status = 201
    response['meta']['status'] = status
    benchmark_end = time.time()
    response['meta']['execution_time'] = benchmark_end - benchmark_start
    return build_response(response, status=status)


@csrf_exempt
@login_required
def api_birthday_pay(request):
    benchmark_start = time.time()
    response = prepare_response(request)
    status = 200
    birthday_id = request.POST['birthday_id']
    if birthday_id:
        try:
            birthday = Birthday.objects.get(id=birthday_id)
            response['birthday_id'] = birthday_id
            contribution = BirthdayContribution.objects.get(birthday=birthday, contributor=request.user)
            amount = float(request.POST['amount'])
            if amount > 0.0:
                contribution.amount += amount
            contribution.save()
            response['amount'] = amount
            response['total_amount'] = contribution.amount
            response['birthday_contribution_id'] = contribution.id
            birthday.amount_raised += amount
            birthday.save()
        except Birthday.DoesNotExist:
            status = 404
    else:
        status = 400
    response['meta']['status'] = status
    benchmark_end = time.time()
    response['meta']['execution_time'] = benchmark_end - benchmark_start
    return build_response(response, status=status)

def index(request):
    if not request.user.is_authenticated():
        context = RequestContext(request)
        return render_to_response('index.html', context)

    return HttpResponseRedirect('/home')

@login_required
def home(request):
    tpl = loader.get_template('home.html')
    return HttpResponse(tpl.render(RequestContext(request, {})))

@login_required
def birthday(request):
    tpl = loader.get_template('birthday.html')
    return HttpResponse(tpl.render(RequestContext(request, {})))