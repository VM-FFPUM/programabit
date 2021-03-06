# Generated by Django 3.0.3 on 2020-04-18 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registrar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_limite', models.DateField()),
                ('precio_estimado', models.CharField(max_length=8)),
                ('zona', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('habilidades_requeridas', models.CharField(max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oferta', models.CharField(max_length=8)),
                ('tiempo_estimado', models.CharField(max_length=30)),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicar.Anuncio')),
            ],
        ),
    ]
