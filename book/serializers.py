from rest_framework import serializers

from authentication.models import User
from .models import Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'id')


class BookSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Book
        fields = "__all__"


