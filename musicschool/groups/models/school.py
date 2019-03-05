from django.db import models
from django.contrib.auth.models import User
from .article import Article
from .media import Media
from .category import Category


class School(models.Model):
    name 		= models.CharField(max_length=30)
    address     = models.CharField(max_length=50)
    phone       = models.CharField(max_length=20)
    article     = models.ManyToManyField(
        "Article", 
        verbose_name = "Articles",
        blank = True
    )
    group       = models.ManyToManyField(
        "MemberGroup", 
        verbose_name = "Groupes",
        blank = True
    )
    media       = models.ManyToManyField(
        "Media", 
        verbose_name = "Médias",
        blank = True
    )


class SchoolRight(models.Model):
    PROF    = 'Prof'
    STUDENT = 'Student' 
    LEVEL_USER_CHOICES = (
        (PROF, PROF),
        (STUDENT, STUDENT)
    )
    
    erp_user =   models.ForeignKey(
        'ERPUser', 
        on_delete=models.CASCADE
    ) 
    school  =   models.ForeignKey(
        'School', 
        on_delete=models.CASCADE
    )    
    level   =   models.CharField(
        max_length=20, 
        choices=LEVEL_USER_CHOICES, 
        default=STUDENT
    )
