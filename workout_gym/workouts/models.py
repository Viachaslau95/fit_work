from django.db import models


class Workouts(models.Model):
    type_of_training = models.CharField('Type of training', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return f'Workouts:{self.type_of_training}'

    def get_absolute_url(self):
        return f'/workouts/{self.id}'

    class Meta:
        verbose_name = 'Workouts'
        verbose_name_plural = 'Workouts'