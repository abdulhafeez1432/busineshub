# Generated by Django 3.2 on 2021-04-28 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutbusiness',
            name='business',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='about', to='seller.business'),
        ),
    ]
