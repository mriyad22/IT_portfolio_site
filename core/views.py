from django.shortcuts import render, redirect
from services.models import ServiceModel
from portfolio.models import ProjectModel
from team.models import TestimonialModel
from blog.models import PostModel

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard:index")
    
    services = ServiceModel.objects.filter(is_active=True).order_by("order", "title")[:6]
    projects = ProjectModel.objects.filter(is_published=True).order_by("-featured", "-created_at")[:3]
    testimonials = TestimonialModel.objects.filter(is_active=True).order_by("order")[:3]
    posts = PostModel.objects.filter(is_published=True).order_by("-published_at", "-created_at")[:3]

    context = {
        "services": services, 
        "projects": projects,
        "testimonials": testimonials, 
        "posts": posts,
    }
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)
