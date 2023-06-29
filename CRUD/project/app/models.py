from django.db import models

# Create your models here.


class Created(models.Model):
    name = models.CharField(max_length= 10000)
    
    def __str__(self):
        return self.name