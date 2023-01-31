from django.db import models

# Create your models here.

class employeedb(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    designation = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
class categorydb(models.Model):
    category_name= models.CharField(max_length=30, null=True, blank=True)
    discription= models.CharField(max_length=30, null=True, blank=True)
    image= models.ImageField(upload_to="profile", null=True, blank=True)
class productdb(models.Model):
    category= models.CharField(max_length=30, null=True, blank=True)
    productname = models.CharField(max_length=30,null=True, blank=True)
    discription = models.CharField(max_length=100, null=True, blank=True)
    productprice = models.IntegerField(null=True, blank=True)

    image = models.ImageField(upload_to="profile", null=True, blank=True)

