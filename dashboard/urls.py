from django.urls import path
from .views import *

app_name = "dashboard"
urlpatterns = [
    #-----> Index page URL
    path("", index, name="index"),

    #-----> Service, Project, TeamMember, and Post model CRUD operation URL
    path("content/<slug:content_type>/", content_list, name="content_list"),
    path("content/<slug:content_type>/add/", content_create, name="content_create"),
    path("content/<slug:content_type>/<int:pk>/edit/", content_edit, name="content_edit"),
    path("content/<slug:content_type>/<int:pk>/delete/", content_delete, name="content_delete"),

    #-----> Contact URL
    path("messages/", contact_messages, name="contact_messages"),
    path("messages/<int:pk>/toggle-read/", toggle_message_read, name="toggle_message_read"),
]
