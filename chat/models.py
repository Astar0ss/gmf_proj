from django.db import models

class ChatMessage(models.Model):
    author_name = models.CharField(max_length=100)
    message_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author_name
