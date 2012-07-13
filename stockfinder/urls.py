from django.conf.urls import patterns, include, url

urlpatterns = patterns('stockfinder.views',
	url(r'^(?P<ticker>(.+))/$', 'stockfinder_view'),
    )