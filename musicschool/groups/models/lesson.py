from datetime import date, timedelta, datetime
from django.db import models
from .userinformation import ERPUser


class LessonDate(models.Model):
    date = models.DateField()
    lesson = models.ForeignKey(
        'Lessons',
         related_name='dates', 
         on_delete=models.CASCADE,
         null=True
    )


class Lessons(models.Model):
    user = models.OneToOneField(
        "ERPUser", 
        on_delete=models.CASCADE
    )

    DAY_OF_THE_WEEK = {
        '1' : 'Monday',
        '2' : 'Tuesday',
        '3' : 'Wednesday',
        '4' : 'Thursday',
        '5' : 'Friday',
        '6' : 'Saturday', 
        '7' : 'Sunday',
    }

    def get_3_next_lesson(self):
        next_date_in_3_weeks = datetime.today() + timedelta(days=21)
        all_dates = []
        for date in self.dates.all().order_by('date'):
            if len(all_dates) > 2:
                break;
            if date.date > datetime.today().date():
                all_dates.append(date)
        return(all_dates)

    def get_next_lesson(self):
        all_dates = []
        for date in self.dates.all():
            if date.date > datetime.today().date():
                all_dates.append(date)
        return(all_dates)

'''
en premier trouver le chiffre du jour 
boucler pour arriver au premier chiffre 
puis fait time_delta de une semaine jusqu'a  
arriver à la même date avec un timedelta d'un an de plus
'''