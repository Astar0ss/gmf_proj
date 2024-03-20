from django.shortcuts import render


def chat_room(request):
    return request('chatroom.html',{'chat_messages': chat_messages})