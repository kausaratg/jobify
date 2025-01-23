from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('chatbot', views.chatbot, name = "chatbot"),
    path('login', views.login, name = "login"),
    path('register', views.register, name = "register"),
    path('logout', views.logout, name = "logout"),
    path('analyser', views.analyse_cv, name = "analyser"),
]
