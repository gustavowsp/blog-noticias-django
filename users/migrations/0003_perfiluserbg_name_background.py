# Generated by Django 4.2.5 on 2023-10-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_perfiluserbg'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfiluserbg',
            name='name_background',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
