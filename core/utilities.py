from django.utils import simplejson
from django.http import HttpResponse
import random
from django.conf import settings
from django.contrib.auth import load_backend, login


# Status Codes: http://en.wikipedia.org/wiki/List_of_HTTP_status_codes
def build_response(response, mimetype='application/json', status=200):
    return HttpResponse(simplejson.dumps(response), mimetype=mimetype, status=status)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    return client_ip


def prepare_response(request):
    response = {}
    meta_data = {}
    meta_data['request_uri'] = request.build_absolute_uri()
    meta_data['get'] = request.GET
    meta_data['post'] = request.POST
    meta_data['ip'] = get_client_ip(request)
    if 'sessionid' in request.COOKIES:
        meta_data['session_id'] = request.COOKIES['sessionid']
    if 'csrftoken' in request.COOKIES:
        meta_data['csrf_token'] = request.COOKIES['csrftoken']
    meta_data['user_agent'] = request.META['HTTP_USER_AGENT']
    if request.user.is_authenticated():
        meta_data['current_user_id'] = request.user.id
    response['meta'] = meta_data
    return response


def get_domain(request):
    domain = 'http://' + request.META['HTTP_HOST']
    return domain


def random_string(max_length=10, chars=list('abcdefghijklmnopqrstuvwxyz0123456789-')):
    min_length = 6
    if max_length < min_length:
        max_length = min_length
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(chars) for i in range(length))


def instant_login(request, user):
    '''
    Log in a user without requiring credentials
    '''
    if not hasattr(user, 'backend'):
        for backend in settings.AUTHENTICATION_BACKENDS:
            if user == load_backend(backend).get_user(user.pk):
                user.backend = backend
                break
    if hasattr(user, 'backend'):
        return login(request, user)
