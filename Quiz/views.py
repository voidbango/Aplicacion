from django.shortcuts import render



# Create your views here.
def inicio(request):
    context = {
        'bienvenido': 'Bienvenido'
    }
    return render(request, 'inicio.html', context)