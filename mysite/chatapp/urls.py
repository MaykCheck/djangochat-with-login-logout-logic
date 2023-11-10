from django.contrib import admin
from django.urls import path
from chatapp import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.index,
         name='index'),
    path('login/',views.user_login,
         name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='chatapp/index.html'),
         name='logout'),
    path('<slug:slug>/',views.chatroom,
         name='chatroom'),
    
]
