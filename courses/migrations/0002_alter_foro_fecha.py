# Generated by Django 4.2.5 on 2023-11-16 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foro',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]