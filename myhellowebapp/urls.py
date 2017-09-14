from collection.backends import MyRegistrationView
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import (
   password_reset, 
   password_reset_done,
   password_reset_confirm,
   password_reset_complete,
   password_change,
   password_change_done,
)
from django.views.generic import (TemplateView, 
    RedirectView,
)

from django.contrib import admin
from django.views.generic import TemplateView #imports so we don't need a view

from collection import views # this imports my views from my collection app

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$', 
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^post/new/$', 
        views.post_new, 
        name='post_new'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.post_detail, 
        name='post_detail'),
    url(r'^post/(?P<slug>[-\w]+)/edit/$', 
        views.edit_post,
        name='edit_post'),
    url(r'^post/(?P<slug>[-\w]+)/publish/$',
        views.post_publish, 
        name='post_publish'),
    url(r'^post/(?P<slug>[-\w]+)/remove/$', 
        views.post_remove, 
        name='post_remove'),
    url(r'^post/(?P<slug>[-\w]+)/privacy/$', 
        views.post_privacy, 
        name='post_privacy'),   
    url(r'^posts/(?P<slug>[-\w]+)/edit/images/$',
        views.edit_post_uploads, name='edit_post_uploads'),
    url(r'^accounts/password/reset/$', 
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^accounts/password/change/$', password_change, {
        'template_name': 'registration/password_change_form.html'}, 
        name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done, 
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', 
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'^accounts/register/$', 
        MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/', 
        include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,\
{
            'document_root': settings.MEDIA_ROOT,
    })
        ]


"""
note that it could also lay out like this if it is less confusing: 

urlpatterns = [
    url(
        regex=r'^$', # beginning of the URL pattern
        view=views.index, #use the index view in views.py in our app
        name='home', #optional- allows us to assign a name to this URL so we can refer to it in the future as "home"
    ),
    url(r'^admin/', admin.site.urls),
]

"""
"""
Template View: 
 Instead of pointing to a function in views.py though, we're going to use 
 Django's generic view called TemplateView that basically says, 
 "Hey, just display this template."
 """