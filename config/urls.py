from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.static import serve
from django.urls import path, include, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("services/", include("services.urls")),
    path("projects/", include("portfolio.urls")),
    path("team/", include("team.urls")),
    path("insights/", include("blog.urls")),
    path("contact/", include("contact.urls")),
    path("dashboard/", include("dashboard.urls")),
    
    path("404-preview/", TemplateView.as_view(template_name="404.html"), name="404_preview"),
]

urlpatterns +=  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
urlpatterns +=  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

handler404 = "core.views.custom_404"
