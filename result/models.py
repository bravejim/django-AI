from django.db import models

# Create your models here.
class Disease(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=120)
    description = models.TextField()
    medication = models.TextField(blank=True)
    source = models.CharField(max_length=120,default="Kementerian Kesehatan")
    imageUrl = models.CharField(max_length=120,default="/static/images/diseases")