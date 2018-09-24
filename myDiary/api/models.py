from django.db import models

class Entries(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
