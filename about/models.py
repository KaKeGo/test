from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(upload_to='about/')
    
    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return f'{self.title}'
