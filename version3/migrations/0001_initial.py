# Generated by Django 3.0.3 on 2020-02-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id_chofer', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_chofer', models.CharField(max_length=120)),
                ('description_chofer', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'choferes',
            },
        ),
    ]
