# Generated by Django 5.1.1 on 2024-09-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20200419_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=18941, unique=True),
        ),
        migrations.AlterField(
            model_name='emergencycontactdetails',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='enrolledstudent',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='guardianinfo',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='previousacademiccertificate',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='previousacademicinfo',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentaddressinfo',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
