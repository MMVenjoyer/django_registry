from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from establishment.models import Establishment
from main.settings import AUTH_USER_MODEL


class TrainerQueryset(models.QuerySet):
    def get_trainer_by_lastname(self, lastname: str):
        return self.filter(lastname=lastname)
    

    def get_trainer_by_name(self, name: str):
        return self.filter(name=name)
    

    def get_trainer_by_fathername(self, fathername: str):
        return self.filter(fathername=fathername)
    
    
    def get_trainer_by_study_place(self, study_place: str):
        return self.filter(study_place=study_place)


    def get_trainer_by_iin(self, iin: int):
        return self.filter(iin=iin)
    

class TrainerManager(models.Manager):
    def get_queryset(self):
        return TrainerQueryset(self.model)
    

    def get_trainer_by_lastname(self, lastname: str):
        return self.get_queryset().get_trainer_by_lastname(lastname)
    

    def get_trainer_by_name(self, name: str):
        return self.get_queryset().get_trainer_by_name(name)
    

    def get_trainer_by_fathername(self, fathername: str):
        return self.get_queryset().get_trainer_by_fathername(fathername)
    
    
    def get_trainer_by_study_place(self, study_place: str):
        return self.get_queryset().get_trainer_by_study_place(study_place)


    def get_trainer_by_iin(self, iin: int):
        return self.get_queryset().get_trainer_by_iin(iin)
    

    def save_trainer(self,
                    lastname: str,
                    name: str,
                    fathername: str,
                    contact_phone: str,
                    contact_email: str,
                    iin: int,
                    work_place: str):
        trainer = self.get_or_create(lastname=lastname,
                              name=name,
                              fathername=fathername,
                              contact_phone=contact_phone,
                              contact_email=contact_email,
                              iin=iin,
                              work_place=work_place)
        return trainer
    

class Trainer(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    fathername = models.CharField(max_length=255)
    contact_phone = PhoneNumberField(null=False, blank=False, unique=True)
    contact_email = models.EmailField(max_length=254)
    iin = models.IntegerField(null=False, unique=True)
    photo = models.ImageField() 
    work_place = models.ForeignKey(Establishment, on_delete = models.CASCADE)

    objects = models.Manager()
    trainer_mng = TrainerManager()


    def __str__(self) -> str:
        return self.name