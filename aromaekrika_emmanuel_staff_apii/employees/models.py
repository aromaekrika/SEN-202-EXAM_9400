from django.db import models

# Create your models here.

class StaffBase(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Manager(models.Manager):
        manager_name =models.CharField(max_length=100)
        department =models.CharField(max_length=100)
        has_company_card = models.BooleanField(default=True)



    class Intern(models.Manager):
        Intern_name =models.CharField(max_length=100)
        mentor =models.CharField(max_length=100)
        internship_end = models.DateField





