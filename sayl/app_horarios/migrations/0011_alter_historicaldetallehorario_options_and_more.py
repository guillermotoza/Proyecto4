# Generated by Django 5.1.2 on 2024-11-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_horarios', '0010_auto_20200102_0912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaldetallehorario',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical detalle horario', 'verbose_name_plural': 'historical detalle horarios'},
        ),
        migrations.AlterModelOptions(
            name='historicalhorario',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical horario', 'verbose_name_plural': 'historical horarios'},
        ),
        migrations.AlterModelOptions(
            name='historicalhorariosfijos',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical horarios fijos', 'verbose_name_plural': 'historical horarios fijoss'},
        ),
        migrations.AlterModelOptions(
            name='historicalperiodolectivo',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical periodo lectivo', 'verbose_name_plural': 'historical periodo lectivos'},
        ),
        migrations.AlterField(
            model_name='historicaldetallehorario',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalhorario',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalhorariosfijos',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalperiodolectivo',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
