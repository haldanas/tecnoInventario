# Generated by Django 3.2.9 on 2021-12-04 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('referencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(db_column='a_codigo', primary_key=True, serialize=False)),
                ('nombre', models.TextField(db_column='a_nombre', max_length=50)),
                ('direccion', models.TextField(db_column='a_direccion', max_length=100)),
                ('creado', models.DateField(auto_now_add=True, db_column='a_creado')),
                ('modificado', models.DateField(auto_now=True, db_column='a_modificado')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(db_column='i_cantidad', default=0)),
                ('creado', models.DateField(auto_now_add=True, db_column='i_creado')),
                ('modificado', models.DateField(auto_now=True, db_column='i_modificado')),
                ('almacen', models.ForeignKey(db_column='a_codigo', on_delete=django.db.models.deletion.CASCADE, to='almacenes.almacen')),
                ('referencia', models.ForeignKey(db_column='r_codigo', on_delete=django.db.models.deletion.CASCADE, to='referencias.referencia')),
            ],
        ),
        migrations.AddField(
            model_name='almacen',
            name='referencias',
            field=models.ManyToManyField(through='almacenes.Inventario', to='referencias.Referencia'),
        ),
    ]
