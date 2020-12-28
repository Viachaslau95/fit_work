# Generated by Django 3.1.3 on 2020-12-28 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20201225_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/%Y/%m/'),
            preserve_default=False,
        ),
    ]