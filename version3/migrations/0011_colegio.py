# Generated by Django 3.0.3 on 2020-03-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version3', '0010_auto_20200307_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id_colegio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_colegio', models.CharField(max_length=120)),
                ('direccion_colegio', models.CharField(default=0, max_length=120)),
            ],
            options={
                'verbose_name_plural': 'colegios',
            },
        ),
    ]
