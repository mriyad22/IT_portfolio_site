from django.db import models
from django.urls import reverse
from django.utils.text import slugify

#-------> Managing website services
class ServiceModel(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    short_description = models.CharField(max_length=240)
    description = models.TextField()
    icon_class = models.CharField(max_length=80, blank=True, help_text="Bootstrap Icons class, e.g. bi-code-slash")
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "service"
            candidate, counter = base, 2
            while ServiceModel.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{counter}"
                counter += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("services:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
