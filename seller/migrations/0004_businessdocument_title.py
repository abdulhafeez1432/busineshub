# Generated by Django 3.2 on 2021-04-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_businesstaff_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdocument',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
