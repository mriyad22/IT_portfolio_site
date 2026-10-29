from django.shortcuts import get_object_or_404, render
from .models import PostModel

def post_list(request):
    posts = PostModel.objects.filter(is_published=True)

    context = {
        "posts": posts
    }
    return render(request, "blog/post_list.html", context)



def post_detail(request, slug):
    post = get_object_or_404(PostModel, slug=slug, is_published=True)

    context = {
        "post": post
    }
    return render(request, "blog/post_detail.html", context)
