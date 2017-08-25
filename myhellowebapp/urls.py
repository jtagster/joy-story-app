from django.conf.urls import url
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
    url(r'^things/(?P<slug>[-\w]+)/$', views.thing_detail, 
        name='thing_detail'),    
    url(r'^things/(?P<slug>[-\w]+)/edit/$', 
        views.edit_thing,
        name='edit_thing'),
    url(r'^admin/', admin.site.urls),
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