# Generated by Django 5.0.7 on 2024-08-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_alter_church_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='year_founded',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
