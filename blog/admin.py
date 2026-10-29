from django.contrib import admin
from .models import PostModel

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "is_published", "published_at")
    list_filter = ("is_published", "published_at")
    search_fields = ("title", "excerpt", "body")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_published",)
    date_hierarchy = "published_at"
