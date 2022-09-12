from django.urls import path
from . import views

app_name = "spongebob"

urlpatterns=[
    path("", views.sponge, name="sponge")
]