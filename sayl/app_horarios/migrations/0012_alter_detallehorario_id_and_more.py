# Generated by Django 5.1.2 on 2024-11-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_horarios', '0011_alter_historicaldetallehorario_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallehorario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicaldetallehorario',
            name='id',
            field=models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicalhorario',
            name='id',
            field=models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicalhorariosfijos',
            name='id',
            field=models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicalperiodolectivo',
            name='id',
            field=models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='horariosfijos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='periodolectivo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
