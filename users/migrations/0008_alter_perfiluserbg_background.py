# Generated by Django 4.2.5 on 2023-10-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_backgrounddashboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiluserbg',
            name='background',
            field=models.ImageField(upload_to='dashboard_bg'),
        ),
    ]
