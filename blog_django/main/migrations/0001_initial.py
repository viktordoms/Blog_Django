# Generated by Django 4.0 on 2021-12-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Користувач', help_text="Введіть своє ім'я", max_length=20, verbose_name="Ім'я")),
                ('last_name', models.CharField(help_text='Введіть своє прізвище', max_length=20, verbose_name="Ім'я")),
                ('email', models.EmailField(help_text='Введіть свій е-маіл', max_length=40, verbose_name='Email')),
                ('password', models.CharField(help_text='Введіть пароль', max_length=25, verbose_name='Пароль')),
            ],
        ),
    ]
