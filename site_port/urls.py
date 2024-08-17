from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #Caminho base da view do app
]