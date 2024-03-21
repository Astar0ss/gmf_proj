from django.shortcuts import render, redirect
from .models import ChatMessage
from .forms import ChatMessageForm

def chat_room(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat_room')
    else:
        form = ChatMessageForm()
    return render(request, 'chat_room.html', {'form': form, 'chat_messages': ChatMessage.objects.all()})

def send_message(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat_room')
    else:
        form = ChatMessageForm()
    return render(request, 'send_message.html', {'form': form})



