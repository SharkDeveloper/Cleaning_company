from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Clients(models.Model):
    name = models.CharField("ФИО",max_length=50)
    email = models.EmailField("Эл.почта",max_length=50)
    phone = PhoneNumberField("Телефон",max_length=50)
    password = models.CharField("Пароль", max_length=20)

    def __str__(self) -> str:
        return self.name
    
    #переименование в админпанали название таблицы
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиент"

class Order(models.Model):
    name = models.CharField("Имя",max_length=50)
    surename = models.CharField("Фамилия",max_length=50)
    email = models.EmailField("Эл.почта",max_length=50)
    phone = models.TextField("Телефон",max_length=11)
    review = models.TextField("Напишите отзыв здесь")
    rec_choices = models.TextChoices("Green","Red")
    recommendation = models.CharField(max_length=5)
    suggestion = models.TextField("Что бы вы изменили в работе?")

    def __str__(self) -> str:
        return self.email
    
    #переименование в админпанали название таблицы
    class Meta:
        verbose_name = "Рекоментация"
        verbose_name_plural = "Рекомендации"