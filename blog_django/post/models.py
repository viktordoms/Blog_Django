from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    text = models.TextField("Текст поста", blank=True)
    photo = models.ImageField("Фото", upload_to='photos/%Y/%m/%d', null=True)
    time_create = models.DateTimeField("Дата створення", auto_now_add=True)
    time_update = models.DateTimeField("Дата редагування", auto_now=True)
    is_published = models.BooleanField("Публікування", default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категорія")
    likes = models.ManyToManyField(User, related_name="blog_posts")
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"
        ordering = ['-time_create']

    def get_absolute_url(self):
        return reverse('post', kwargs={"post_slug": self.slug})


class Category(models.Model):
    name = models.CharField('Категорія', max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

