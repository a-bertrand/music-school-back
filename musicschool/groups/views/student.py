from django.views.generic import View
from musicschool.libs.logged_view import LoggedStudentView
from django.shortcuts import redirect, render
from  musicschool.groups.models import MemberGroup, Media, Article


class StudentView(View):
    template_name = 'strudent/home.html'

    def get(self, request):
        if request.user:
            if request.user.is_staff:
                return redirect('/admin')
            elif request.user.is_authenticated:
                membergroup = MemberGroup.objects.filter(members=request.user.user_information).first()
                return render(
                    request, 
                    self.template_name,
                    {
                        'membergroup':membergroup,
                    }
                )
            else:
                return redirect('login')
        else:
            return redirect('login')
