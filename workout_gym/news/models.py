from django.db import models

from datetime import datetime


class Articles(models.Model):
    title = models.CharField(max_length=250)
    anons = models.CharField(max_length=250)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    pub_date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return f'News:{self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'