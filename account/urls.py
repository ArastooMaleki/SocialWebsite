from django.urls import path
from django.contrib.auth import views
# from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
]
