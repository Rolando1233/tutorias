# Generated by Django 5.0.6 on 2024-06-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('Enero - Abril', 'Enero - Abril'), ('Mayo - Agosto', 'Mayo - Agosto'), ('Septiembre - Diciembre', 'Septiembre - Diciembre')], max_length=22, verbose_name='Periodo')),
                ('year', models.IntegerField(default=2024, verbose_name='Año')),
                ('cycle', models.CharField(default='2024-2025', max_length=20, verbose_name='Ciclo')),
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Periodo',
                'verbose_name_plural': 'Periodos',
                'ordering': ['year'],
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=2, verbose_name='Cuatrimestre')),
                ('semester_name', models.CharField(max_length=10, verbose_name='Cuatrimestre en Letra')),
                ('short_name', models.CharField(max_length=5, verbose_name='Abreviatura')),
            ],
            options={
                'verbose_name': 'Cuatrimestre',
                'verbose_name_plural': 'Cuatrimestres',
            },
        ),
    ]
