from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    text = models.TextField("Текст поста", blank=True)
    photo = models.ImageField("Фото", upload_to='photos/%Y/%m/%d', null=True)
    time_create = models.DateTimeField("Дата створення", auto_now_add=True)
    time_update = models.DateTimeField("Дата редагування", auto_now=True)
    is_published = models.BooleanField("Публікування", default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"
        ordering = ['time_create']

    def get_absolute_url(self):
        return reverse('post', kwargs={"post_id": self.pk})


class Category(models.Model):
    name = models.CharField('Категорія', max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
