# Generated by Django 2.1.7 on 2019-03-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weeks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='week',
            name='abbrev',
        ),
        migrations.RemoveField(
            model_name='week',
            name='name',
        ),
        migrations.RemoveField(
            model_name='week',
            name='site',
        ),
        migrations.AddField(
            model_name='week',
            name='week_char',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='week',
            name='week_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
