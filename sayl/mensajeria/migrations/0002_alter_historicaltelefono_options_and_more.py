# Generated by Django 5.1.2 on 2024-11-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaltelefono',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical telefono', 'verbose_name_plural': 'historical telefonos'},
        ),
        migrations.AlterField(
            model_name='historicaltelefono',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]