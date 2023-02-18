from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    number=models.CharField(max_length=10)
    title=models.CharField(max_length=150)
    subject=models.TextField()
    
    def __str__(self):
        return self.title


class Consultant(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.fullname