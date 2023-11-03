from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# Create your models here.

class Consumed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Food(models.Model):

  name = models.CharField(max_length=100)
  carbs = models.FloatField()
  protein = models.FloatField()
  fats = models.FloatField()
  calories = models.IntegerField()
  food_consumed = models.ForeignKey(Consumed, related_name='foods', on_delete=models.CASCADE)

  def __str__(self):
    return self.name


    



