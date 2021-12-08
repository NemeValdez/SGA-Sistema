# Generated by Django 3.2.9 on 2021-12-08 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carreras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstudiantesInscripcionesCompletas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Inscripción general',
                'verbose_name_plural': 'Inscripciones formalizadas',
            },
        ),
        migrations.CreateModel(
            name='EstudiantesPrimerCarrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Inscripción formalizada',
                'verbose_name_plural': 'Inscripciones formalizadas',
            },
        ),
        migrations.CreateModel(
            name='EstudiantesSegundaCarrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Inscripción formalizada',
                'verbose_name_plural': 'Inscripciones formalizadas',
            },
        ),
        migrations.CreateModel(
            name='Inscripciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateTimeField(verbose_name='Fecha y hora de la preinscripción')),
            ],
            options={
                'verbose_name': 'Dato de Inscripción',
                'verbose_name_plural': 'Datos de Inscripciones',
            },
        ),
        migrations.CreateModel(
            name='InstitutosCarreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contador_aceptados', models.PositiveIntegerField(default=0)),
                ('contador_lista_espera', models.PositiveIntegerField(default=0)),
                ('relacion_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrerasInscripcion', to='carreras.carreras')),
            ],
            options={
                'verbose_name': 'Relación entre Instituto y Carrera',
                'verbose_name_plural': 'Relaciones entre Institutos y Carreras',
            },
        ),
    ]
