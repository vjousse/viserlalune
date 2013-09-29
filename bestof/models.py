from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    description = models.TextField()
