from django.shortcuts import render, get_object_or_404
from .models import Post
#Vista de blog
def render_posts(request): #Primera vista del blog 
    articulos = Post.objects.all()
    return render(request, 'posts.html', {'posts':articulos})
def post_detail(request, post_id): #Vista del blog parte de los detalles
    post = get_object_or_404(Post, pk=post_id)
    #El metodo render pide el nombre de la plantilla
    return render(request, 'post_detail.html', {"post":post})
