# Now we are supposed to define the URL path for the django and pytube function

from django.contrib import admin 
from django.urls import path 
from . import views 

urlpatterns = [ 
	path('riddhi/', admin.site.urls), 
	path('youtube', views.youtube, name='youtube'), 
]
