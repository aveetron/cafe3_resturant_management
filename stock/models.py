from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name