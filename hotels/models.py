from django.db import models
from cloudinary.models import CloudinaryField

class Hotel(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image')
    description = models.CharField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
