from django.contrib.auth.models import Group, User
from rest_framework import serializers
from core import models


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']