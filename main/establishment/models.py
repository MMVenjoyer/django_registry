from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from main.settings import AUTH_USER_MODEL


class Establishment(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    region = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    adrees = models.CharField(max_length=255)
    contact_phone = PhoneNumberField(null=False, blank=False, unique=True)
    contact_email = models.EmailField(max_length=254)

    objects = models.Manager()


    def __str__(self) -> str:
        return self.name