# Generated by Django 3.2.9 on 2021-12-03 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.CharField(db_column='m_codigo', max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.TextField(db_column='m_nombre', max_length=50)),
                ('operador', models.CharField(db_column='m_operador', max_length=5)),
                ('tipo', models.CharField(choices=[('S', 'Suma'), ('R', 'Resta'), ('O', 'Opeara')], db_column='m_tipo', default='O', max_length=2)),
                ('creado', models.DateField(auto_now_add=True, db_column='m_creado')),
                ('modificado', models.DateField(auto_now=True, db_column='m_modificado')),
            ],
        ),
    ]
