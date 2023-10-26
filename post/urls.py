from django.urls import path

from .views import (coment)

urlpatterns = [
    path('comentarios/', coment, name = 'comentar')
]