from django.shortcuts import get_object_or_404, render
from .models import ServiceModel

def service_list(request):
    services = ServiceModel.objects.filter(is_active=True)

    context = {
        "services": services
    }
    return render(request, "services/service_list.html", context)


def service_detail(request, slug):
    service = get_object_or_404(ServiceModel, slug=slug, is_active=True)
    related_services = ServiceModel.objects.filter(is_active=True).exclude(pk=service.pk)[:3]

    context = {
        "service": service, 
        "related_services": related_services
    }
    return render(request, "services/service_detail.html", context)
