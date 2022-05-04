from django.contrib import admin
from django.urls import path 
from . import views
app_name = "article"
urlpatterns = [
    path("addarticle/",views.addarticle,name="addarticle"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("detail/<int:id>",views.detail,name="detail"),

 ]
