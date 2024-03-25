from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from establishment.models import Establishment
from user.models import CustomUser


class StudentQueryset(models.QuerySet):
    def get_student_by_lastname(self, lastname: str):
        return self.filter(lastname=lastname)
    

    def get_student_by_name(self, name: str):
        return self.filter(name=name)
    

    def get_student_by_fathername(self, fathername: str):
        return self.filter(fathername=fathername)
    
    
    def get_student_by_study_place(self, study_place: str):
        return self.filter(study_place=study_place)


    def get_student_by_iin(self, iin: int):
        return self.filter(iin=iin)
    

class StudentManager(models.Manager):
    def get_queryset(self):
        return StudentQueryset(self.model)
    

    def get_student_by_lastname(self, lastname: str):
        return self.get_queryset().get_student_by_lastname(lastname)
    

    def get_student_by_name(self, name: str):
        return self.get_queryset().get_student_by_name(name)
    

    def get_student_by_fathername(self, fathername: str):
        return self.get_queryset().get_student_by_fathername(fathername)
    
    
    def get_student_by_study_place(self, study_place: str):
        return self.get_queryset().get_student_by_study_place(study_place)


    def get_student_by_iin(self, iin: int):
        return self.get_queryset().get_student_by_iin(iin)
    

class Student(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    fathername = models.CharField(max_length=255)
    contact_phone = PhoneNumberField(null=False, blank=False, unique=True)
    contact_email = models.EmailField(max_length=254)
    iin = models.IntegerField(null=False, unique=True)
    photo = models.ImageField()
    section = models.CharField(choices=Establishment.Section.choices, max_length=255)
    study_place = models.ForeignKey(Establishment, on_delete = models.CASCADE) # Надо сделать автопостановку учреждения опираясь на id пользователя из запроса

    objects = models.Manager()
    student_mng = StudentManager()


    def __str__(self) -> str:
        return self.name