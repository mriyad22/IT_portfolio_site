from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.db.models import Q

from blog.models import PostModel
from contact.models import ContactMessageModel
from services.models import ServiceModel
from portfolio.models import ProjectModel
from team.models import *
from .forms import CONTENT_MODELS, get_content_form


#-----> Create a decorator for user restricted
def staff_required(view_func):
    """Only authenticated staff users may access content management."""
    @login_required(login_url="/admin/login/")
    @wraps(view_func)
    def wrapped(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("Staff access is required.")
        return view_func(request, *args, **kwargs)
    return wrapped


#--> Locating the configuration for a specific Content Type within the CONTENT_MODELS dictionary and verifying its validity.
def get_content_config(content_type):
    config = CONTENT_MODELS.get(content_type)
    if config is None:
        raise PermissionDenied("Unknown content type.")
    return config


#----> overView page View
@staff_required
def index(request):
    modules = []
    for key, config in CONTENT_MODELS.items():
        model = config["model"]
        modules.append({**config, "key": key, "count": model.objects.count(), "url": reverse("dashboard:content_list", kwargs={"content_type": key})})

    # print(modules)
    context = {
        "modules": modules,
        "services_count": ServiceModel.objects.count(),
        "projects_count": ProjectModel.objects.count(),
        "posts_count": PostModel.objects.count(),
        "messages_count": ContactMessageModel.objects.filter(is_read=False).count(),
        "recent_messages": ContactMessageModel.objects.all()[:5],
    }
    return render(request, "dashboard/index.html", context)


#------> Content list View
@staff_required
def content_list(request, content_type):
    config = get_content_config(content_type)
    queryset = config["model"].objects.all()
    
    search = request.GET.get("q", "").strip()
    if search:
         #-->Specifying which fields to search in
        searchable = [f.name    #--> 'f.name' Provides the field name as a string.
            for f in config["model"]._meta.fields 
            if getattr(
                f, "get_internal_type", lambda: ""
            )() in {"CharField", "TextField", "SlugField"}
        ]

        # print(searchable)
        
        query = Q()
        for field_name in searchable:
            query |= Q(**{f"{field_name}__icontains": search})
        if searchable:
            queryset = queryset.filter(query)

    context = {
        "config": config, 
        "content_type": content_type, 
        "objects": queryset, 
        "search": search
    }
    return render(request, "dashboard/content_list.html", context)


#--------> Content create View
@staff_required
def content_create(request, content_type):
    config = get_content_config(content_type)
    form_class = get_content_form(config["model"])

    form = form_class(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save()
        messages.success(request, f'{config["singular"].capitalize()} created successfully.')
        return redirect("dashboard:content_list", content_type=content_type)

    context = {
        "config": config, 
        "content_type": content_type, 
        "form": form, 
        "page_title": f'Add {config["singular"]}'

    }
    return render(request, "dashboard/content_form.html", context)


#------> Content edit View
@staff_required
def content_edit(request, content_type, pk):
    config = get_content_config(content_type)
    obj = get_object_or_404(config["model"], pk=pk)
    form_class = get_content_form(config["model"])

    form = form_class(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f'{config["singular"].capitalize()} updated successfully.')
        return redirect("dashboard:content_list", content_type=content_type)

    context = {
        "config": config, 
        "content_type": content_type, 
        "form": form, 
        "page_title": f'Edit {config["singular"]}', 
        "object": obj
    }
    return render(request, "dashboard/content_form.html", context)


#------>Specific Content delete View
@staff_required
def content_delete(request, content_type, pk):
    config = get_content_config(content_type)
    obj = get_object_or_404(config["model"], pk=pk)

    if request.method == "POST":
        obj.delete()
        messages.success(request, f'{config["singular"].capitalize()} deleted successfully.')
        return redirect("dashboard:content_list", content_type=content_type)

    context = {
        "config": config, 
        "content_type": content_type, 
        "object": obj
    }
    return render(request, "dashboard/content_confirm_delete.html", context)


#-----> Display all messages View
@staff_required
def contact_messages(request):
    messages_qs = ContactMessageModel.objects.all()

    context = {
        "contact_messages": messages_qs
    }
    return render(request, "dashboard/contact_messages.html", context)


#------> Toggle message read View
@staff_required
@require_POST
def toggle_message_read(request, pk):
    obj = get_object_or_404(ContactMessageModel, pk=pk)
    obj.is_read = not obj.is_read
    obj.save(update_fields=["is_read"])
    
    messages.success(request, "Message status updated.")
    return redirect("dashboard:contact_messages")