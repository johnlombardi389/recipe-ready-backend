# Generated by Django 4.2.5 on 2023-09-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeready', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]