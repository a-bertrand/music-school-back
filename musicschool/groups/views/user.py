from django.views.generic.base import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from datetime import date, timedelta, datetime
from musicschool.groups.models import (
    ERPUser, 
    Lessons,
    LessonDate,
    School, 
    SchoolRight, 
)
from django.shortcuts import get_object_or_404
from musicschool.groups.forms import UserForm


class RegistrationView(View):
    template_name = "registration/signup.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            erp_user = ERPUser(
                phonenumber=request.POST['phone'],
                adress=request.POST['adress'],
                user=user
            )
            user.save()
            erp_user.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()


class UserListView(View):
    template_name = "prof/users/user_list.html"

    def get(self, request):
        users = ERPUser.objects.all()
        return render(
            request, 
            self.template_name,
             {'users': users}
        )


class UserManageView(View):
    template_name = "prof/users/user_add_edit.html"

    def get(self, request, user_id = None):
        
        if user_id:
            erp_user = get_object_or_404(ERPUser, pk=user_id)
            user_form = UserForm(instance=erp_user)
            return render(
                request, 
                self.template_name,
                {
                   'user_form': user_form,
                   'erp_user': erp_user
                }
            ) 
        else:
            user_form = UserForm()
            return render(
                request, 
                self.template_name,
                {
                    'user_form': user_form
                }
            ) 

    def post(self, request, user_id = None):
        if request.POST.get('is_lesson_date'):
            if request.POST.get('is_lesson_date') == "on" and request.POST.get('lesson_date'):
                erp_user = get_object_or_404(ERPUser, pk=user_id)
                if Lessons.objects.filter(user=erp_user).first():
                    Lessons.objects.filter(user=erp_user).first().delete()
                date = datetime.strptime(request.POST.get('lesson_date'), '%Y-%m-%d')
                self.create_a_year_of_lesson(date, erp_user)

        if user_id:
            erp_user = get_object_or_404(ERPUser, pk=user_id)
            if request.POST.get('activate_student') and request.POST.get('activate_student') == "on" :
                # TODO multiple SCHOOL
                school = School.objects.first()
                school_right = SchoolRight(erp_user=erp_user, school=school, level=SchoolRight.STUDENT)
                school_right.save()
            user_form = UserForm(request.POST or None, instance=erp_user)
        else:
            user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user-list')

    # asked the date of the first lesson
    def create_a_year_of_lesson(self, date_of_the_first_lesson, erp_user):
        new_lessons = Lessons(user=erp_user)
        new_lessons.save()
        next_date_year = date_of_the_first_lesson + timedelta(days=365)
        index = 0
        while index < 52:
            add_day = index * 7
            date_to_add = date_of_the_first_lesson + timedelta(days=add_day) 
            date = LessonDate(date=date_to_add)
            date.save()
            new_lessons.dates.add(date)
            index = index + 1;
            # au cas zou
            if index > 52:
                break;
        new_lessons.save()

class UserDeleteView(View):
    pass

