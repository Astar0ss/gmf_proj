from django.db import models

# Create your models here.
class Message(models.Model):
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    message_text = models.TextField()
    date_posted = models.DateTimeField()

def __str__(self):
    return self.author_name