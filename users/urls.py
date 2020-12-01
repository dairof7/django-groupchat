from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('message-list/', views.MessageList.as_view(), name='message_list'),
    path('user-message-list/<kword>', views.UserMessageList.as_view(), name='user_message_list'),
    path('user-list/', views.UserList.as_view(), name='user_list'),
]