from . import views
from django.urls import path
urlpatterns =[
    path('mails/',views.send_emails,name='send_emails'),
]