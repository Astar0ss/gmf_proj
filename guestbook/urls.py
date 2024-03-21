from django.urls import path
from . import views

urlpatterns = [
    path('', views.guestbook_list, name='guestbook_list'),
    path('add/', views.add_message, name='add_message'),
]
