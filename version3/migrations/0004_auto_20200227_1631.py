# Generated by Django 3.0.3 on 2020-02-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version3', '0003_contrato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='id',
        ),
        migrations.AddField(
            model_name='contrato',
            name='id_usuario',
            field=models.IntegerField(default=66565),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contrato',
            name='id_contrato',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]