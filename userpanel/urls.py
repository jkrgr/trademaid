from django.conf.urls import patterns, include, url

urlpatterns = patterns('userpanel.views',
    (r'^$', 'userpanel_view'),
    (r'^new_user', 'new_user_view'),
)
