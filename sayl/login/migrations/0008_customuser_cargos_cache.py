# Generated by Django 2.2.5 on 2020-01-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0005_remove_cargoscache_agente'),
        ('login', '0007_remove_customuser_cargos_cache'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cargos_cache',
            field=models.ManyToManyField(to='cargos.CargosCache'),
        ),
    ]
