from django.db import models


class Users(models.Model,):
    __tablename__ = 'users'
    first_name = models.CharField("Ім'я", max_length=20, default="Користувач", help_text="Введіть своє ім'я")
    last_name = models.CharField("Прізвище", max_length=20, help_text="Введіть своє прізвище")
    email = models.EmailField("Email", max_length=40, help_text="Введіть свій е-маіл")
    password = models.CharField("Пароль", max_length=25, help_text="Введіть пароль")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

