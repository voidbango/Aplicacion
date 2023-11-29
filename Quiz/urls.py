from django.urls import path

from .views import (
	inicio, 
	registro, 
	loginView, 
	logout_vista,
	HomeUsuario, 
	jugar,
	resultado_pregunta,
	tablero,
	puntaje_individual,
	user_statistics
)

urlpatterns = [
	
	path('', inicio, name='inicio'),
	path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),


	path('login/', loginView, name='login'),
	path('logout_vista/', logout_vista, name='logout_vista'),
	path('registro/', registro, name='registro'),
	path('tablero/', tablero, name='tablero'),
	path('puntaje_individual/', puntaje_individual, name='puntaje_individual'),
	path('user-statistics/', user_statistics, name='user_statistics'),
	
	path('jugar/', jugar, name='jugar'),
	path('resultado/<int:pregunta_respondida_pk>/', resultado_pregunta, name='resultado'),

]