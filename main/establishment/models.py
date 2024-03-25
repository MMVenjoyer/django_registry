from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from user.models import CustomUser


class Establishment(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    region = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    adrees = models.CharField(max_length=255)
    contact_phone = PhoneNumberField(null=False, blank=False, unique=True)
    contact_email = models.EmailField(max_length=254)

    objects = models.Manager()


    class Section(models.TextChoices):
        boxing = 'Бокс', 'Бокс'
        swimming = 'Плавание', 'Плавание'
        weightlifting = 'Тяжелая атлетика', 'Тяжелая атлетика'
        athletics = 'Легкая атлетика', 'Легкая атлетика'
        wrestling = 'Борьба', 'Борьба'
        greco_roman_wrestling = 'Греко-римская борьба', 'Греко-римская борьба'


    def __str__(self) -> str:
        return self.name