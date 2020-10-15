from django.db import models

# Create your models here.
class Asia(models.Model):
    city = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    population = models.IntegerField()

    def __str__(self):
        return self.city

class America(models.Model):
    city = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    population = models.IntegerField()

    def __str__(self):
        return self.city

class Africa(models.Model):
    city = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    population = models.IntegerField()

    def __str__(self):
        return self.city

class Europe(models.Model):
    city = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    population = models.IntegerField()

    def __str__(self):
        return self.city