from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerir/',views.power,name="powerir"),
    path('',views.power,name="powerir")


]