# Generated by Django 4.1.1 on 2023-05-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='question',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
