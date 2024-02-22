from django.db import models

# Create your models here.


class MenuHeader(models.Model):
    title = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.title
