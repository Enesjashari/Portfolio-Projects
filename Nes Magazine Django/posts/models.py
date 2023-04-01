from distutils.command.upload import upload
from email.policy import default
from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField



# Create your models here.

class Tech(models.Model):
    title = models.CharField(max_length=555)
    prefix = models.CharField(max_length=320,default = None,blank=True)
    body = models.CharField(max_length=10000)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body2 = models.CharField(max_length=10000 , blank=True , default=" ")
    image2 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body3 = models.CharField(max_length=10000 , blank=True , default=" ")
    image3 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    category = models.CharField(max_length=1000,default = None)
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    video = EmbedVideoField( blank=True , default=" ")  # same like models.URLField()

    def __str__(self):
        return self.title[:]


class HeaderPost(models.Model):
    title = models.CharField(max_length=555)
    body = models.CharField(max_length=10000)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body2 = models.CharField(max_length=10000 , blank=True , default=" ")
    image2 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body3 = models.CharField(max_length=10000 , blank=True , default=" ")
    image3 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    category = models.CharField(max_length=1000,default = None)
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    video = EmbedVideoField( blank=True , default=" ")  # same like models.URLField()
    def __str__(self):
        return self.title[:]

class Showbiz(models.Model):
    title = models.CharField(max_length=555)
    body = models.CharField(max_length=10000)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body2 = models.CharField(max_length=10000 , blank=True , default=" ")
    image2 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body3 = models.CharField(max_length=10000 , blank=True , default=" ")
    image3 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    category = models.CharField(max_length=1000,default = "Showbiz")
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    video = EmbedVideoField( blank=True , default=" ")  # same like models.URLField()

    def __str__(self):
        return self.title[:]


class Travel(models.Model):
    title = models.CharField(max_length=555)
    body = models.CharField(max_length=10000)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body2 = models.CharField(max_length=10000 , blank=True , default=" ")
    image2 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body3 = models.CharField(max_length=10000 , blank=True , default=" ")
    image3 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    category = models.CharField(max_length=1000,default = "Travel")
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    video = EmbedVideoField( blank=True,default=" ")  # same like models.URLField()

    def __str__(self):
        return self.title[:]

class Sport(models.Model):
    title = models.CharField(max_length=555)
    body = models.CharField(max_length=10000)
    image = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body2 = models.CharField(max_length=10000 , blank=True , default=" ")
    image2 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    body3 = models.CharField(max_length=10000 , blank=True , default=" ")
    image3 = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    category = models.CharField(max_length=1000,default = "Sport")
    created_at =models.DateTimeField(default=datetime.now, blank=True)
    video = EmbedVideoField( blank=True , default=" ")  # same like models.URLField()

    def __str__(self):
        return self.title[:]


class Video(models.Model):
    name = models.CharField(max_length=555)
    text_url = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=500)

    def __str__(self):
        return self.name[:]
