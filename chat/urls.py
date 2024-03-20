from django.urls import path
from . import views
from ..guestbook.views import guestbook_list

urlpatterns = [
    path('chat/', views.chat_room, name="chat_form"),
    path('guestbook/',guestbook_list,name="guestbook_list")
]

