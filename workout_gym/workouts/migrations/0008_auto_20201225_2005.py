# Generated by Django 3.1.3 on 2020-12-25 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0007_auto_20201225_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workouts',
            old_name='full_text',
            new_name='text',
        ),
    ]