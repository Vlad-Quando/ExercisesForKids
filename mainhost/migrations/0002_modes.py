# Generated by Django 5.0 on 2024-01-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainhost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=100, verbose_name='Режим')),
            ],
            options={
                'verbose_name': 'Режим',
                'verbose_name_plural': 'Режимы',
            },
        ),
    ]