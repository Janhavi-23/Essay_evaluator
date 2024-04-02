from django.db import models

class Essay(models.Model):
    title = models.CharField(max_length=100)
    body_text = models.TextField(max_length=500)

# Create your models here.
