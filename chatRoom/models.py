from django.db import models
from django.contrib.auth.models import User
# from django.urls.base import User

# Create your models here.


class Room(models.Model):

    """Модель комнаты чата"""

    creater = models.ForeignKey(User, verbose_name='creater', on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name='Participant', related_name="invited_user")
    date = models.DateTimeField("Create date", auto_now_add=True)

    class Meta:

        verbose_name = "Chat room"
        verbose_name_plural = "Chat Rooms"


class Chat(models.Model):

    """Chat model"""

    room = models.ForeignKey(Room, verbose_name="Chat room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Message sent", auto_now_add=True)

    class Meta:
        verbose_name = "Message chat"
        verbose_name_plural = "Messages chats"
