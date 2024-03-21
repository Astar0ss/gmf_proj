from django import forms
from .models import GuestbookMessage

class GuestbookMessageForm(forms.ModelForm):
    class Meta:
        model = GuestbookMessage
        fields = ['author_name', 'author_email', 'message_text']
