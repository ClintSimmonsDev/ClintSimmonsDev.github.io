# Generated by Django 2.1.5 on 2019-06-19 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelogue', '0002_auto_20190617_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Mysterio', max_length=25),
        ),
    ]
