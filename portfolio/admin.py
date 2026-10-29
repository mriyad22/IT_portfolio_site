from django.contrib import admin
from .models import ProjectModel

@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "is_published", "created_at")
    list_filter = ("category", "featured", "is_published")
    search_fields = ("title", "summary", "description", "technologies")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("featured", "is_published")
