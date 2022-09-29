from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts1 = Post.objects.all().order_by('-pk')
    return render(request, 'blog/index.html', {'posts': posts1})

def single_post_page(request, pk):
    post2 = Post.objects.get(pk=pk)
    return render(request, 'blog/single_post_page.html', {'post':post2})