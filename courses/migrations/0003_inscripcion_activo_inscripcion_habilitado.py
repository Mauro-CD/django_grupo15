# Generated by Django 4.2.5 on 2023-11-18 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_foro_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='habilitado',
            field=models.BooleanField(default=False),
        ),
    ]