from django.shortcuts import get_object_or_404, render
from .models import ProjectModel, ProjectCatgoryModel



def project_list(request):
    projects = ProjectModel.objects.filter(is_published=True)

    category = request.GET.get("category", "").strip()

    if category:
        projects = projects.filter(category__name__iexact=category)

    categories = ProjectCatgoryModel.objects.filter(project_category__is_published=True).values_list("name", flat=True).distinct().order_by("name")

    context = {
        "projects": projects,
        "categories": categories,
        "selected_category": category,
    }
    return render(request, "portfolio/project_list.html", context)



def project_detail(request, slug):
    project = get_object_or_404(ProjectModel, slug=slug, is_published=True)
    related_projects = ProjectModel.objects.filter(is_published=True, category=project.category).exclude(pk=project.pk)[:3]

    context = {
        "project": project, 
        "related_projects": related_projects
    }
    return render(request, "portfolio/project_detail.html", context)
