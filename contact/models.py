from django.db import models

# Create your models here.


class Contact(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    email = models.EmailField()
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    discord = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.title}'
