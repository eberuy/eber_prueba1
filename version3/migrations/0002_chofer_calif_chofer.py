# Generated by Django 3.0.3 on 2020-02-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chofer',
            name='calif_chofer',
            field=models.IntegerField(default=3),
        ),
    ]