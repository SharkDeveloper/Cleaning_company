from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Clients(models.Model):
    name = models.CharField("ФИО", max_length=50)
    login = models.CharField("Логин",max_length=50)
    email = models.EmailField("Эл.почта", max_length=50)
    phone = models.CharField("Телефон", max_length=11)
    password = models.CharField("Пароль", max_length=20)

    def __str__(self) -> str:
        return self.name

    # переименование в админпанали название таблицы
    class Meta:
        verbose_name = "клиента"
        verbose_name_plural = "Клиенты"


class Orders(models.Model):
    author = models.ForeignKey(Clients, on_delete=models.CASCADE)
    data = models.DateField("Дата заказа")
    type_cleaning = models.CharField("Вариант уборки",max_length=50)
    status = models.CharField("Статус заказа",max_length=50)
    price = models.IntegerField("Цена услуги")

    # переименование в админпанали название таблицы
    class Meta:
        verbose_name = "закаказ"
        verbose_name_plural = "Заказы"

