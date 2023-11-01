from django.urls import path
from .views import post_idd, comentario_id, eliminarComentarios


urlpatterns=[
    path('post_id/<int:pk>/', post_idd, name='post_idd'),
    path('comentario_id/<int:pk>/', comentario_id, name='comentario_id'),
    path('eliminar/<int:id>/', eliminarComentarios, name='eliminar')
]