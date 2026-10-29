from django import forms
from django.forms import modelform_factory

from services.models import ServiceModel
from portfolio.models import ProjectModel, ProjectCatgoryModel
from team.models import *
from blog.models import PostModel
from contact.models import ServiceCategoryModel


"""
Four pieces of information are provided for each content type:
    - model: The Django model it will work with.
    - title: The name displayed in the admin panel.
    - singular: The singular name for an individual item.
    - description: A description of the purpose for which that content type is used.

What is the advantage of CONTENT_MODELS?

Instead of writing separate admin views or configurations for every piece of content, 
you can use this dictionary to create a reusable or dynamic view/template. 
For example, you could manage Services, Projects, Team Members, and Blog Posts all from the same admin page.

In short: CONTENT_MODELS is a central configuration dictionary for various Django models, which helps make the custom admin panel dynamic and easy to maintain.
"""
CONTENT_MODELS = {
    "services": {"model": ServiceModel, "title": "Services", "singular": "service", "description": "Manage services shown on your website."},
    "projects": {"model": ProjectModel, "title": "Projects", "singular": "project", "description": "Publish portfolio projects and case studies."},
    "team": {"model": TeamMemberModel, "title": "Team members", "singular": "team member", "description": "Manage company team profiles."},
    "testimonials": {"model": TestimonialModel, "title": "Testimonials", "singular": "testimonial", "description": "Manage client reviews and ratings."},
    "insights": {"model": PostModel, "title": "Insights / Blog posts", "singular": "post", "description": "Write, edit, publish or unpublish articles."},
    "servicecategory": {"model": ServiceCategoryModel, "title": "Service category", "singular": "service category", "description": "Manage Service Category for Contact."},
    "projectcategory" : {'model': ProjectCatgoryModel, 'title':'Project Category', 'singular': "project category", "description":"Manage Project Category."}
}


def get_content_form(model_class):
    """Build a ModelForm for an allow-listed content model, excluding automatic fields."""
    excluded = []
    for field in model_class._meta.fields:  #--> Information about the fields of a model can be obtained using 'ModelName._meta.fields', 'ModelName._meta.model_name', and 'ModelName._meta.app_label' .
        if field.auto_created or field.name in {"created_at", "updated_at", "published_at"}:
            excluded.append(field.name)
    # published_at is managed automatically when a post is published.
    return modelform_factory(model_class, form=forms.ModelForm, exclude=excluded)

    """
    'modelform_factory()' is used to create a `ModelForm` class based on a given model.

    Its arguments are:
        - model_class: The model for which the form is to be created.
        - form=forms.ModelForm: Uses the standard `ModelForm` as a base.
        - exclude=excluded: Excludes the fields listed in the `excluded` list from the form.
    """


"""
The job of this get_content_form(model_class) function is to automatically create a ModelForm for any specific Django Model, 
where specific fields like created_at, updated_at, published_at will not be displayed in the form.

It is commonly used in Custom Admin Panel or CMS, 
where forms for Service, Project, TeamMember, Testimonial etc. models can be created with the same code.
"""