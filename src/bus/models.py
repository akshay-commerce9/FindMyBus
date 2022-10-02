from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User_reg(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class Owner_reg(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class Complaint(models.Model):
    bus_no = models.CharField(max_length=15)
    complaint = models.CharField(max_length=250)

class Bus(models.Model):
    oid = models.ForeignKey(Owner_reg,on_delete=models.CASCADE)
    bus_name = models.CharField(max_length=30)
    bus_no = models.CharField(max_length=15)
    bus_img = models.FileField()

class Route(models.Model):
    bus_id = models.ForeignKey(Bus,on_delete=models.CASCADE)
    first_st = models.CharField(max_length=50)
    stops = ArrayField(models.CharField(max_length=200), blank=True)
    last_st = models.CharField(max_length=50)
    first_ti = models.CharField(max_length=50)
    times = ArrayField(models.CharField(max_length=200), blank=True)
    last_ti = models.CharField(max_length=50)


class Places(models.Model):
    place = models.CharField(max_length=50,unique=True)

