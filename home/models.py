from django.db import models

# Create your models here.
class Question(models.Model):
    code = models.CharField(max_length=4, default="this is cool")
    description = models.TextField(default="this is cool")
