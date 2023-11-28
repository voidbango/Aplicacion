from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from .forms import RegistroFormulario, UsuarioLoginFormulario

from .models import QuizUsuario, Pregunta, PreguntasRespondidas, ElegirRespuesta
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

def inicio(request):

	context = {

		'bienvenido': 'Bienvenido'

	}

	return render(request, 'inicio.html', context)


def HomeUsuario(request):

	return render(request, 'Usuario/home.html')


def tablero(request):
	total_usaurios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
	contador = total_usaurios_quiz.count()

	context = {

		'usuario_quiz':total_usaurios_quiz,
		'contar_user':contador
	}

	return render(request, 'play/tablero.html', context)

def jugar(request):

	QuizUserr, created = QuizUsuario.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_respondida = QuizUserr.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
		respuesta_pk = request.POST.get('respuesta_pk')

		try:
			opcion_selecionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
		except ObjectDoesNotExist:
			raise Http404

		QuizUserr.validar_intento(pregunta_respondida, opcion_selecionada)

		return redirect('resultado', pregunta_respondida.pk)

	else:
		pregunta = QuizUserr.obtener_nuevas_preguntas()
		if pregunta is not None:
			QuizUserr.crear_intentos(pregunta)

		context = {
			'pregunta':pregunta
		}

	return render(request, 'play/jugar.html', context)



def resultado_pregunta(request, pregunta_respondida_pk):
	respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

	context = {
		'respondida':respondida
	}
	return render(request, 'play/resultados.html', context)

def loginView(request):
	titulo = 'login'
	form = UsuarioLoginFormulario(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		usuario = authenticate(username=username, password=password)
		login(request, usuario)
		return redirect('HomeUsuario')

	context = {
		'form':form,
		'titulo':titulo
	}

	return render(request, 'Usuario/login.html', context)

def registro(request):

	titulo = 'Crear una Cuenta'
	if request.method == 'POST':
		form = RegistroFormulario(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegistroFormulario()

	context = {

		'form':form,
		'titulo': titulo

	}

	return render(request, 'Usuario/registro.html', context)


def logout_vista(request):
	logout(request)
	return redirect('/')



def puntaje_individual(request):
    # Obtén el puntaje total del usuario actual
    usuario_actual = request.user
    puntaje_usuario_actual = 0

    try:
        quiz_usuario = QuizUsuario.objects.get(usuario=usuario_actual)
        puntaje_usuario_actual = quiz_usuario.puntaje_total
    except QuizUsuario.DoesNotExist:
        pass

    context = {
        'usuario_actual': usuario_actual,
        'puntaje_usuario_actual': puntaje_usuario_actual,
    }

    return render(request, 'play/puntaje_individual.html', context)
