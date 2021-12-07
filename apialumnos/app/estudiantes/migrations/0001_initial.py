# Generated by Django 3.2.9 on 2021-12-07 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstudiantesEstablecimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_escuela', models.CharField(max_length=100, verbose_name='Nombre del secundario del preinscripto')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título que otorga el secundario')),
                ('estado_secundario', models.CharField(max_length=1, verbose_name='Estado de la finalización del secundario')),
            ],
            options={
                'verbose_name': 'Secundario del Estudiante',
                'verbose_name_plural': 'Secundario del Estudiante',
            },
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_estudiante', models.CharField(max_length=100, verbose_name='Apellido del estudiante')),
                ('nombre_estudiante', models.CharField(max_length=100, verbose_name='Nombre del estudiante')),
                ('dni_estudiante', models.CharField(max_length=8, verbose_name='DNI del estudiante')),
                ('sexo_estudiante', models.CharField(max_length=1, verbose_name='Sexo del estudiante')),
                ('provincia_estudiante', models.CharField(max_length=100, verbose_name='Provincia de residencia del estudiante')),
                ('telefono_estudiante', models.CharField(max_length=50, verbose_name='Teléfono del estudiante')),
                ('mail_estudiante', models.EmailField(max_length=254, verbose_name='Mail del estudiante')),
                ('legajo_estudiante', models.CharField(max_length=12, verbose_name='Número de legajo del estudiante')),
                ('secundario_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secundariasEstudiantes', to='estudiantes.estudiantesestablecimientos')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
    ]