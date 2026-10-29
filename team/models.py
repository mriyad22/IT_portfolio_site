from django.db import models

#-----> Managing team member profiles
class TeamMemberModel(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="team/", blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} — {self.role}"

    
#------> Managing client reviews and ratings
class TestimonialModel(models.Model):
    client_name = models.CharField(max_length=100)
    company = models.CharField(max_length=120, blank=True)
    role = models.CharField(max_length=100, blank=True)
    quote = models.TextField()
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)])
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "client_name"]

    def __str__(self):
        return f"{self.client_name} testimonial"
