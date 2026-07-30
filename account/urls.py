from django.contrib.auth import views
from django.urls import path

from .views import dashoboard

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path(
        "change-password/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "change-password/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("", dashoboard, name="dashboard"),
]
