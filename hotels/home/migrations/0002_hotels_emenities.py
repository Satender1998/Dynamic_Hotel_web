# Generated by Django 4.1.4 on 2022-12-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='emenities',
            field=models.ManyToManyField(to='home.emenities'),
        ),
    ]
