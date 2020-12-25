from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Workouts(models.Model):
    type_of_training = models.CharField(max_length=50)
    anons = models.CharField(max_length=250)
    text = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'Workouts:{self.type_of_training}'

    def get_absolute_url(self):
        return f'/workouts/{self.id}'

    class Meta:
        verbose_name = 'Workouts'
        verbose_name_plural = 'Workouts'