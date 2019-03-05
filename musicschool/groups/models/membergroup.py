from django.db import models
from .userinformation import ERPUser
from .article import Article

class MemberGroup(models.Model):
    name   		= models.CharField(max_length=30)
    members 	= models.ManyToManyField(ERPUser, related_name='members_group')
    articles	= models.ManyToManyField(Article, related_name='articles_group')

    def __str__(self):
        return self.name
