from core.models import OBUser
from django.views.decorators.csrf import csrf_exempt
from core.forms import get_validation_errors, UserRegisterForm
from core.utilities import build_response, prepare_response, get_domain
import time
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
import urllib
from django.http import HttpResponseRedirect
from django.contrib import auth


def facebook_login(request):
    # TODO: Add CSRF prevention
    login_link = 'https://www.facebook.com/dialog/oauth?' + urllib.urlencode(
        {
            'client_id': settings.FACEBOOK_APP_ID,
            'redirect_uri': get_domain(request) + '/',
            'response_type': 'code',
            'scope': 'email',
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
        new_user = OBUser(email=data['email'])
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


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)
