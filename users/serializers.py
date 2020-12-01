from rest_framework import serializers, pagination
from .models import Messages, Users

class UsersSerializer(serializers.ModelSerializer):
    # we have to use many because is a many to many relation
    class Meta:
        model = Users
        fields = ('__all__')


class AllMessageSerializer(serializers.ModelSerializer):
    # we have to use many because is a many to many relation
    class Meta:
        model = Messages
        fields = ('__all__')

class Pagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 10