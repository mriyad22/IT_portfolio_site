from django.shortcuts import get_object_or_404, render

from .models import ProjectCatgoryModel, ProjectModel


def project_list(request):
    projects = ProjectModel.objects.filter(is_published=True).select_related("category")
    category = request.GET.get("category", "").strip()

    if category:
        projects = projects.filter(category__name__iexact=category)

    categories = (
        ProjectCatgoryModel.objects.filter(project_category__is_published=True)
        .order_by("name")
        .values_list("name", flat=True)
        .distinct()
    )

    context = {
        "projects": projects,
        "categories": categories,
        "selected_category": category,
    }
    return render(request, "portfolio/project_list.html", context)


def project_detail(request, slug):
    project = get_object_or_404(
        ProjectModel.objects.select_related("category"),
        slug=slug,
        is_published=True,
    )

    related_projects = ProjectModel.objects.filter(is_published=True).exclude(pk=project.pk)
    if project.category_id:
        related_projects = related_projects.filter(category_id=project.category_id)
    else:
        related_projects = related_projects.none()
    related_projects = related_projects.select_related("category")[:3]

    context = {
        "project": project,
        "related_projects": related_projects,
    }
    return render(request, "portfolio/project_detail.html", context)
