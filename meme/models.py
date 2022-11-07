from django.db import models

# Create your models here.


class MeMe(models.Model):
    title = models.CharField(max_length=70)
    img = models.ImageField(upload_to='meme')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    category = models.ManyToManyField('Category', related_name='category')
    filters = models.ManyToManyField('MeMeFilters', related_name='meme_filters')
    create_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        ordering = ['-create_on']
        verbose_name_plural = 'Memes'
        verbose_name = 'Meme'
        
    def __str__(self):
        return f'{self.title} / {self.id}'

class Category(models.Model):
    title = models.CharField(max_length=70)
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
            
    def __str__(self):
        return str(self.title)

class MeMeFilters(models.Model):
    title = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'MeMeFiters'
        verbose_name = 'MeMeFiter'
            
    def __str__(self):
        return str(self.title)
