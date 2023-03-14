from django.db import models


class Person(models.Model):
    name = models.CharField(verbose_name='Ім\'я', max_length=300, help_text='Enter your name please!')
    age = models.IntegerField(verbose_name='Вік')
    phone_number = models.IntegerField(verbose_name='Номер телефону')
    address = models.CharField(verbose_name='Адреса', max_length=300, blank=True)
    place_location = models.URLField(verbose_name='Місце знаходження',
                                     help_text='You must add http reference your location from google maps',
                                     max_length=700, blank=True)

    def __str__(self):
        return self.name
