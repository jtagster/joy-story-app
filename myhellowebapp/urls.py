from django.conf.urls import url
from django.contrib import admin

from collection import views # this imports my views from my collection app

urlpatterns = [
    url(r'^$', views.index, name='home'),
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