from django.db import models

from users.models import User


class Country(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False, unique=True, verbose_name='Страна')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='country_address_set', db_index=True, null=False, blank=False)
    city = models.TextField(max_length=50, null=False, blank=False, verbose_name='Город')
    street = models.TextField(max_length=50, null=False, blank=False, verbose_name='Улица')
    house = models.TextField(max_length=10, null=False, blank=False, verbose_name='Дом')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.country}, г. {self.city}, ул. {self.street}, д. {self.house}'


class Contacts(models.Model):
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True, verbose_name='Эл. почта')
    address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                related_name='contacts_address_set', db_index=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.email} | {self.address}'


class Products(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False, verbose_name='Название продукта')
    prod_model = models.TextField(max_length=50, null=False, blank=False, verbose_name='Модель')
    release_date = models.DateField(null=False, blank=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} {self.prod_model}'


class SellersNetwork(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False, verbose_name='Название компании')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE,
                                 related_name='info_contacts_set', db_index=True, null=False, blank=False,
                                 verbose_name='Контакты')
    products = models.ManyToManyField(Products, related_name='info_products_set', db_index=True,
                                      verbose_name='Продукты')
    workers = models.ManyToManyField(User, related_name='info_workers_set', db_index=True, verbose_name='Работники')
    debt = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='Долг')
    creation_time = models.DateTimeField(auto_now=True, verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'

    def __str__(self):
        return f'{self.name}'
