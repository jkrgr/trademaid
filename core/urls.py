from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin, admindocs
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'core.views.home', name='home'),
    #url(r'^core/portfolio', include('trademaid.core.portfolio.urls')),
    (r'^userpanel/', include('userpanel.urls')),
    (r'^ticker/',include('stockfinder.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
    #(r'^admin/doc/', include('admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', admin.site.urls),
)
