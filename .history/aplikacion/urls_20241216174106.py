from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name=""),
    path("about/", views.about),
    path("contactUs/", views.contact)
]