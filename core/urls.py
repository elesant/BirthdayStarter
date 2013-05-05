from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'index'),
    url(r'^facebook-login/$', 'facebook_login'),
    url(r'^signout/$', 'signout'),
    url(r'^api/user/register/$', 'api_user_register'),

    # requires login
    url(r'^home/$', 'home'),
    url(r'^api/present/parse/$', 'api_present_parse'),
    url(r'^api/friend/list/$', 'api_friend_list'),
)
