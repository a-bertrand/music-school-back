from django.db import models
from django.contrib.auth.models import User
from .school import SchoolRight, School


class ERPUser(models.Model):
    phonenumber	= models.CharField(max_length=30)
    adress      = models.CharField(max_length=50)
    user    = models.OneToOneField(
        User, 
        related_name='user_information',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return  '%s %s' % (self.user.first_name, self.user.last_name)

    #TODO update if multi school
    def get_school_right(self):
        school = School.objects.all().first()
        return SchoolRight.objects.filter(erp_user=self, school=school).first()

    def is_prof(self):
        return self.get_school_right().level == SchoolRight.PROF
    
    def is_student(self):
        return self.get_school_right().level == SchoolRight.STUDENT
    
    def is_activate(self):
        return self.get_school_right() is not None

    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"