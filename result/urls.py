from django.urls import path

from . import views
 
urlpatterns= [
    path('', views.home, name='home'),
    path('details', views.details, name='details'),
    path('enter', views.enter, name='enter')
]