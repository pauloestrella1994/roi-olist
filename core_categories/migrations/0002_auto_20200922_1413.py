# Generated by Django 3.1.1 on 2020-09-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriesroivalue',
            name='roi_value',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
