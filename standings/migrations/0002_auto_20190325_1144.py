# Generated by Django 2.1.7 on 2019-03-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standing',
            name='losses',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='standing',
            name='wins',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]
