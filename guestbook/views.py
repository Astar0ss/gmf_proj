from django.shortcuts import render, redirect
from .models import GuestbookMessage
from .forms import GuestbookMessageForm

def guestbook_list(request):
    messages = GuestbookMessage.objects.all()
    return render(request, 'guestbook_list.html', {'messages': messages})

def add_message(request):
    if request.method == 'POST':
        form = GuestbookMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook_list')
    else:
        form = GuestbookMessageForm()
    return render(request, 'add_message.html', {'form': form})





