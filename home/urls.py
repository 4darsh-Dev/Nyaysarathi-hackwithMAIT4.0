from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact , name="contact"),
    path("services/", views.services , name="services"),
    
    path("login/",views.loginUser, name="loginUser"),
    path("signup/", views.signupUser, name="signupUser"),
    path("logout/", views.logoutUser, name="logout"),

    
]
