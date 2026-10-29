from django.contrib import admin
from .models import ServiceModel

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("title", "short_description", "description")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_active", "order")
