from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title