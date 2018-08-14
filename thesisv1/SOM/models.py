from django.db import models
from django import forms

# Create your models here.

class SOM(models.Model):
    pic_name = models.FileField()
    path = models.CharField(max_length = 500)

    def __str__(self):
        return self.pic_name + ' - ' + self.path

class fileupload(models.Model):
    file_name = forms.CharField(max_length=255)