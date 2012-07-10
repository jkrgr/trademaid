from django.conf.urls import patterns, include, url

urlpatterns = patterns('stockfinder.views',
    (r'^ticker/(?P<ticker>)/$', 'stockfinder_view'),
)