from django.urls import path, re_path
from django.conf.urls import url
from .views import LoginView, ChatView, SignupView, LogoutView, Msg, MsgDel

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('chat/', ChatView, name='chat'),
    path('signup/', SignupView, name='signup'),
    path('logout/', LogoutView, name='logout'),
    path('msg/', Msg, name='message'),
    url(r'^deletemsg/(?P<pk>\d+)/$', MsgDel, name='deletemsg'),
]