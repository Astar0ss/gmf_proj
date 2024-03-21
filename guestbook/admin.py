from django.contrib import admin
from .models import GuestbookMessage

@admin.register(GuestbookMessage)
class GuestbookMessageAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_email', 'date_posted')

