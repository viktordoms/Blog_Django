# Generated by Django 4.0 on 2021-12-21 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_users_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Користувач', 'verbose_name_plural': 'Користувачі'},
        ),
    ]