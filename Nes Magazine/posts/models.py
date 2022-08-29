from distutils.command.upload import upload
from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.

class Tech(models.Model):
    title = models.CharField(max_length=55)
    prefix = models.CharField(max_length=320,default = None,blank=True)
    body = models.CharField(max_length=10000)
    category = models.CharField(max_length=1000,default = None)
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")


    def __str__(self):
        return self.title[:]


class HeaderPost(models.Model):
    title = models.CharField(max_length=55)
    body = models.CharField(max_length=10000)
    category = models.CharField(max_length=1000,default = None)
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")


    def __str__(self):
        return self.title[:]

class Showbiz(models.Model):
    title = models.CharField(max_length=55)
    body = models.CharField(max_length=10000)
    category = models.CharField(max_length=1000,default = "Showbiz")
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")


    def __str__(self):
        return self.title[:]


class Travel(models.Model):
    title = models.CharField(max_length=55)
    body = models.CharField(max_length=10000)
    category = models.CharField(max_length=1000,default = "Travel")
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")


    def __str__(self):
        return self.title[:]

class Sport(models.Model):
    title = models.CharField(max_length=55)
    body = models.CharField(max_length=10000)
    category = models.CharField(max_length=1000,default = "Sport")
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")


    def __str__(self):
        return self.title[:]


