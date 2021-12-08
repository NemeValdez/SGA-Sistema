# Generated by Django 3.2.9 on 2021-12-08 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_instituto', models.CharField(max_length=4, verbose_name='Número del Instituto')),
                ('calle_instituto', models.CharField(max_length=50, verbose_name='Dirección completa del Instituto')),
                ('altura_instituto', models.CharField(max_length=5, verbose_name='Altura de la dirección del Instituto')),
                ('mail_general_instituto', models.EmailField(max_length=254, verbose_name='Mail oficial del Instituto')),
                ('mail_preinscripcion_instituto', models.EmailField(max_length=254, verbose_name='Mail destinado a la preinscripción')),
                ('telefono_instituto', models.CharField(max_length=20, verbose_name='Teléfono del Instituto')),
                ('sitio_web_instituto', models.URLField(blank=True, null=True, verbose_name='Sitio web del Instituto')),
            ],
            options={
                'verbose_name': 'Instituto',
                'verbose_name_plural': 'Institutos',
            },
        ),
        migrations.CreateModel(
            name='InstitutosJerarquicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Responsable e Instituto',
                'verbose_name_plural': 'Responsables y sus Institutos',
            },
        ),
        migrations.CreateModel(
            name='Jerarquicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_jerarquico', models.CharField(max_length=255, verbose_name='Nombre de la persona responsable')),
                ('apellido_jerarquico', models.CharField(max_length=255, verbose_name='Apellido de la persona responsable')),
                ('sexo_jerarquico', models.CharField(blank=True, max_length=1, null=True, verbose_name='Sexo de la persona responsable')),
                ('fecha_nacimiento_jerarquico', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento del responsable')),
            ],
            options={
                'verbose_name': 'Responsable',
                'verbose_name_plural': 'Responsables',
            },
        ),
        migrations.CreateModel(
            name='RolesJerarquicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=100, verbose_name='Rol que desempeña en el Instituto')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos en Sistema',
            },
        ),
        migrations.CreateModel(
            name='SedesInstitutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede_instituto', models.CharField(max_length=100, verbose_name='Nombre de la Sede o Anexo del Instituto')),
                ('calle_sede_instituto', models.CharField(max_length=50, verbose_name='Dirección completa del Instituto')),
                ('altura_sede_instituto', models.CharField(max_length=5, verbose_name='Altura de la dirección del Instituto')),
                ('relacion_instituto_sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sedesInstitutos', to='institutos.institutos')),
            ],
            options={
                'verbose_name': 'Sede del Instituto',
                'verbose_name_plural': 'Sedes del Instituto',
            },
        ),
    ]
