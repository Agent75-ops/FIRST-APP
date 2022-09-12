from . import views
from django.urls import path

app_name="form"

urlpatterns=[
    path("register/", views.index, name="register"),
    path("", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout")
]