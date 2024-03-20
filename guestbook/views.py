from django.shortcuts import render
from chat.models import Message
from .forms import MessageForm
# Create your views here.
def guestbook_list(request):
    messages = Message.object.all()
    return request("guestbook_list.html",{"messages":messages})