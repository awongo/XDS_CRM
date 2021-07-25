from django.urls import path

from . import views

urlpatterns = [
    path("", views.user, name="user"),
    path("user_login", views.user_login, name="User_login"),
    path("user_signup", views.user_signup, name="user_signup")
]
