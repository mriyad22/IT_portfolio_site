from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

#------> Writing, editing, and publishing blog posts
class PostModel(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.CharField(max_length=280)
    body = models.TextField()
    cover_image = models.ImageField(upload_to="blog/", blank=True, null=True)
    author_name = models.CharField(max_length=100, default="IT Solutions Team")
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    """ 
    Its primary function is to automatically generate a unique slug when a post is saved, 
    and to set the `published_at` timestamp when the post is published.

    However, we want certain actions to occur automatically before saving:
        - A slug should be generated from the title.
        - If the slug already exists, a new one should be created.
        - The publication time should be set when a post is published.
    This is why we have written our own `save()` method—a process known as method overriding.
    """
    def save(self, *args, **kwargs):    #---> An object is saved to the database using the built-in `save()` method of a Django model.
        if not self.slug:
            base = slugify(self.title) or "article"     #-->'slugify()' converts a title into a URL-friendly slug.
            candidate, counter = base, 2
            while PostModel.objects.filter(slug=candidate).exclude(pk=self.pk).exists():     #'exclude()' This means: if the current object's own primary key (PK) matches, exclude that object from the results.
                candidate = f"{base}-{counter}"
                counter += 1
            self.slug = candidate
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
