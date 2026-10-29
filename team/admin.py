from django.contrib import admin
from .models import *

@admin.register(TeamMemberModel)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("name", "role", "bio")
    list_editable = ("is_active", "order")

@admin.register(TestimonialModel)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("client_name", "company", "rating", "is_active", "order")
    list_filter = ("rating", "is_active")
    search_fields = ("client_name", "company", "quote")
    list_editable = ("is_active", "order")
