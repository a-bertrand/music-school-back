from django.db import models
from django.contrib.auth.models import User
from .media import Media
from .category import Category



class Article(models.Model):
    title 		= models.CharField(max_length=30)
    content 	= models.CharField(max_length=300)
    categories    = models.ManyToManyField(
        Category, 
        related_name='categories',
        blank=True
    )
    miniature   = models.FileField(upload_to='images', null=True, blank=True )
    media  		= models.ManyToManyField(
        Media, 
        related_name='media',
        blank=True
    )

    def __str__(self):
        return self.title