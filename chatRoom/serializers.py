from rest_framework import serializers
from django.contrib.auth.models import User
from chatRoom.models import Room, Chat


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):

    """ Serializer chat room """
    creater = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ("id", "creater", "invited", "date")


class ChatSerializers(serializers.ModelSerializer):
    """ Serializer chat  """
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = ("id","user", "text", "date")


class ChatPostSerializers(serializers.ModelSerializer):
    """ Serializer chat  """
    class Meta:
        model = Chat
        fields = ("room", "text")
