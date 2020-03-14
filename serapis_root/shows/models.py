from django.db import models
from django import forms


class Show(models.Model):
    class Meta:
        ordering = ['-show_date']

    def __str__(self):
        return str(self.show_date)

    venue = models.CharField(max_length=100)

    show_date = models.DateTimeField()

    city = models.CharField(max_length=100)


class Musician(models.Model):
    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='member_photos')
