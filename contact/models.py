from django.db import models

#----> Service Category Model
class ServiceCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#-----> Contact Message Model
class ContactMessageModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=120, blank=True)
    service = models.ForeignKey(ServiceCategoryModel, on_delete=models.SET_NULL, related_name='category', default='Others', null=True)
    subject = models.CharField(max_length=160)
    message = models.TextField(max_length=5000)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} — {self.name}"