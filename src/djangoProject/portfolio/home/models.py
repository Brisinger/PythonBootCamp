from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(default='', max_length=100)
    phone = models.CharField(default='', max_length=12)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"
