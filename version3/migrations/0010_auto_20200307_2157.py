# Generated by Django 3.0.3 on 2020-03-07 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version3', '0009_auto_20200307_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='direccion',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
