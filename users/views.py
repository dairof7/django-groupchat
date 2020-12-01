from django.shortcuts import render
from .serializers import AllMessageSerializer, UsersSerializer, Pagination
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView
from .models import Messages, Users

class MessageList(ListAPIView):
    # con paginacion
    serializer_class = AllMessageSerializer
    pagination_class = Pagination
    def get_queryset(self):
        return Messages.objects.all()

class UserMessageList(ListAPIView):
    # con paginacion
    serializer_class = AllMessageSerializer
    pagination_class = Pagination
    def get_queryset(self):
        kword = self.kwargs['kword']
        return Messages.objects.filter(user=kword)

class UserList(ListAPIView):
    serializer_class = UsersSerializer
    def get_queryset(self):
        return Users.objects.all()

