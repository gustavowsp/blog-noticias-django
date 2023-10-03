# Generated by Django 4.2.5 on 2023-10-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_perfiluser_dono'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundDashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_background', models.CharField(max_length=200)),
                ('background', models.ImageField(upload_to='perfil_bg')),
                ('utilizar', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Plano de fundo - Dash',
                'verbose_name_plural': 'Planos de fundo - Dash',
            },
        ),
    ]