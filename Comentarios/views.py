from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormComentarios
from .models import Comentarios
from post.models import Post
from django.contrib.contenttypes.models import ContentType

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
        
        comentario, created = Comentarios.objects.get_or_create(
            usuario=request.user,
            content_type=content_type,
            object_id=obj_id,
            texto=texto_data
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
