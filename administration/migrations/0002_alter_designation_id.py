# Generated by Django 5.1.1 on 2024-09-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
