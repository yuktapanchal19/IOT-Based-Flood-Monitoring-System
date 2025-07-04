from django.urls import path
from . import views
#first-argument is what user will type in url
#second will refer to views.py function name

urlpatterns=[
    path('',views.login,name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('register',views.register,name="register"),
    path('waterlevel',views.wl,name="waterlevel"),
    path('rainlevel',views.rl,name="raindrop"),
    path('ultrasoniclevel',views.ul,name="ultrasoniclevel"),
    path('fetchlogindata',views.fetchlogindata,name="fetchlogindata"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('fetchdata',views.fetchdata,name="fetchdata"),
    path('contact', views.contact, name="contactpage"),
    path('error', views.error, name="error")
]
