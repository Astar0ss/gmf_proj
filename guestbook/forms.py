from django import forms
from chat.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['author_name','author_email','message_text']