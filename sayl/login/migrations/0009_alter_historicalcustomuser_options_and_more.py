# Generated by Django 5.1.2 on 2024-11-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_customuser_cargos_cache'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalcustomuser',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical user', 'verbose_name_plural': 'historical users'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='historicalcustomuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='historicalcustomuser',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
