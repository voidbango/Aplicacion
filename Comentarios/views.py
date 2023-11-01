from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormComentarios
from .models import Comentarios
from post.models import Post
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages

def comentario_id(request, pk):
    instance = get_object_or_404(Comentarios, pk=pk)
    context = {
        'comentario': instance
    }
    return render(request, 'comentar/instance.html', context)

def post_idd(request, pk):
    instance = get_object_or_404(Post, pk=pk)

    inicializar_datos = {
        'content_type': ContentType.objects.get_for_model(instance),
        'object_id': instance.id,
    }

    form = FormComentarios(request.POST or None, initial=inicializar_datos)

    if form.is_valid():
        content_type = ContentType.objects.get_for_model(instance)
        obj_id = form.cleaned_data.get('object_id')
        texto_data = form.cleaned_data.get('texto')
        
        padre_obj = None

        try:
            padre_id= int(request.POST.get('padre_identificador'))
        except:
            padre_id= None
        if padre_id:
            padre_qs= Comentarios.objects.filter(id=padre_id)
            if padre_qs.exists() and padre_qs.count()==1:
                padre_obj = padre_qs.first()
                
        comentario, created = Comentarios.objects.get_or_create(
            usuario=request.user,
            content_type=content_type,
            object_id=obj_id,
            texto=texto_data,
            padre= padre_obj
        )

        if created:
            print('Fue creado con éxito')

        # Redirige a la vista "post_idd" después de procesar el comentario.
        return redirect('post_idd', pk=instance.pk)
    
    ver_comentarios= instance.comentarios


    context = {
        'form': form,
        'instance': instance,
        'ver_comentarios': ver_comentarios
    }

    return render(request, 'comentar/comentarios.html', context)

def eliminarComentarios(request, id):
    #instance = get_object_or_404(Comentarios, id=id)
    try:
        instance = Comentarios.objects.get(id=id)
    except:
        raise Http404

    if instance.usuario != request.user:

        response = HttpResponse('Tu No tienes permiso para realizar esta acción')
        response.status_code= 403
        return response

    if request.method == 'POST':
        padre_instance_url= instance.content_objects.get_absolute_url()
        instance.delete()
        messages.success(request, 'Esta acción ha eliminado el comentario')
        return HttpResponseRedirect(padre_instance_url)

    context={

        'instance':instance

    }
    return render(request, 'comentar/eliminar.html', context)