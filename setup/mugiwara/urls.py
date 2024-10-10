from django.urls import path
from mugiwara import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login.as_view(), name="login"),
    path("signup/", views.signup.as_view(), name="signup"),
    path("logout/", views.userLogout, name="logout"),
]
