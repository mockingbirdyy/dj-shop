# Generated by Django 3.2.12 on 2022-03-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
    ]
