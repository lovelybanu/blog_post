from django.urls import path
from . import views
urlpatterns = [
    path("login",views.loginn,name='login'),
    path("register",views.register,name='register'),
    path('home',views.home,name='home'),
    path('logout',views.logoutt,name='signout'),
    path('newpost',views.newPost,name='newpost'),
    path('myposts',views.myposts,name='myposts'),
    path('contactus',views.Contact,name='contact')
]
