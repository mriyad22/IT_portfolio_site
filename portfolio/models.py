from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ProjectCatgoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#-----> Conducting portfolio projects and case studies
class ProjectModel(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    category = models.ForeignKey(ProjectCatgoryModel, on_delete=models.CASCADE, related_name="project_category", null=True)
    client_name = models.CharField(max_length=120, blank=True)
    summary = models.CharField(max_length=250)
    description = models.TextField()
    technologies = models.CharField(max_length=250, blank=True, help_text="Comma-separated, e.g. Django, PostgreSQL, Bootstrap")
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    project_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "project"
            candidate, counter = base, 2
            while ProjectModel.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{counter}"
                counter += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    @property
    def technology_list(self):
        """Return the comma-separated technology field as clean labels."""
        return [item.strip() for item in self.technologies.split(",") if item.strip()]

    def get_absolute_url(self):
        return reverse("portfolio:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
