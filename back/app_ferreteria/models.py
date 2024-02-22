from django.db import models

class CardSelling(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(max_length=None)
    description = models.CharField(max_length=200)
    publication_time = models.DateTimeField()
    sold =models.BooleanField(default=False)