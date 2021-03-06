# Generated by Django 3.2.9 on 2021-11-10 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detalles', '0001_initial'),
        ('referencias', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.perfil'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='registros',
            field=models.ManyToManyField(through='detalles.Registro', to='referencias.Referencia'),
        ),
    ]
