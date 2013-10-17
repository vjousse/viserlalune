from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

class Entry(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField()
    category = models.ForeignKey(Category)
