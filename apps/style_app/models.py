from django.db import models


# Create your models here.


class NavigationBar(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=50)
    def __str__(self):
        return self.name
