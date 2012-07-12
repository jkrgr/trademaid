from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout


urlpatterns = patterns('userpanel.views',
    (r'^$', 'userpanel_view'),
    (r'^new_user', 'new_user_view'),
    (r'^login/$',  login),
    (r'^logout/$', logout),
)
