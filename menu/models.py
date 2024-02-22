from django.db import models

# Create your models here.


class MenuHeader(models.Model):
    title = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    header = models.ForeignKey(MenuHeader, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, unique=True)
    url = models.URLField(blank=True)
    root = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
