# Generated by Django 4.0 on 2021-12-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(help_text='Введіть своє прізвище', max_length=20, verbose_name='Прізвище'),
        ),
    ]
