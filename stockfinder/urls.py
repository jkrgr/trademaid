from django.conf.urls import patterns, include, url

urlpatterns = patterns('stockfinder.views',
    (r'^$', 'stockfinder_view'),
)