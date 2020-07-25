from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
