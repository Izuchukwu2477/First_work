from django.db import models
#the wedsite where uses can buy food
class Food(models.Model):

    price = models.Flootffield(max_length=100,editable=False)
    description = models.TextField(max_length=100)
    images = models.ImageField()
    name = models.CharField(max_length=100)

