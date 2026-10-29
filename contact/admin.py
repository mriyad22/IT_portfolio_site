from django.contrib import admin
from .models import *

@admin.register(ContactMessageModel)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "service", "is_read", "created_at")
    list_filter = ("is_read", "service", "created_at")
    search_fields = ("name", "email", "company", "subject", "message")
    readonly_fields = ("created_at", "ip_address")
    list_editable = ("is_read",)
    date_hierarchy = "created_at"

admin.site.register(ServiceCategoryModel)
