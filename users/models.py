from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    worker_fio = models.TextField(max_length=100, null=False, blank=False, verbose_name='ФИО работника')
    is_working_now = models.BooleanField(default=True, null=False, blank=False, verbose_name='Работает сейчас')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return f'{self.username} {self.worker_fio}'
