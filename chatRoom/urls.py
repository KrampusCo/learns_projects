from django.urls import path
from chatRoom.views import *

urlpatterns = [
    path('rooms/', Rooms.as_view()),
    path('dialog/', Dialog.as_view()),
]
