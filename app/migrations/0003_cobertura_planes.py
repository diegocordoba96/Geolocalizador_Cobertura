# Generated by Django 4.2 on 2023-05-04 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planes', '0001_initial'),
        ('app', '0002_delete_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobertura',
            name='planes',
            field=models.ManyToManyField(to='Planes.plan'),
        ),
    ]
