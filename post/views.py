from django.shortcuts import render
from .models import Post


# Create your views here.
def coment(request):
    todos_los_post=Post.objects.all()
    context ={
        'post':todos_los_post
    }
    return render(request, 'comentar.html', context)