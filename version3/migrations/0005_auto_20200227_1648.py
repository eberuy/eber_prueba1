# Generated by Django 3.0.3 on 2020-02-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version3', '0004_auto_20200227_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='id_usuario',
            field=models.CharField(max_length=60),
        ),
    ]