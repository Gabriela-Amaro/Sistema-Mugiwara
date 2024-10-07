from django.urls import path
from mugiwara import views

urlpatterns = [
    path("", views.index, name="index")
]
