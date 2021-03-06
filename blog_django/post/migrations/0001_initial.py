# Generated by Django 4.0 on 2021-12-22 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категорія')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('text', models.TextField(blank=True, verbose_name='Текст поста')),
                ('photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата редагування')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публікування')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
                'ordering': ['time_create'],
            },
        ),
    ]
