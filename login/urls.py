from django.urls import path
from .views import LoginView, ChatView, SignupView

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('chat/', ChatView, name='chat'),
    path('signup/', SignupView, name='signup'),
]