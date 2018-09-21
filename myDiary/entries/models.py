from django.db import models

class Entry(models.Model):
    entry_id =models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_created=True)