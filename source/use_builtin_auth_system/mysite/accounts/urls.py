from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # user auth urls
    url(r'^login/$',  'views.login', name='login'),
    url(r'^auth/$',  'views.auth_view', name='auth_view'),
    url(r'^logout/$', 'views.logout', name='logout'),
    url(r'^loggedin/$', 'views.loggedin', name='loggedin'),
    url(r'^invalid/$', 'views.invalid_login', name='invalid'),
    url(r'^register/$', 'views.register_user', name='register'),
    url(r'^register_success/$', 'views.register_success', name='register_success'),
)
