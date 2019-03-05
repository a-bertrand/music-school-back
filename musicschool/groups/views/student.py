from django.views.generic import View
from django.shortcuts import redirect, render
from  musicschool.groups.models import MemberGroup, Media, Article


class StudentView(View):
    template_name = 'student/home.html'

    def get(self, request):
        if request.user:
            if request.user.is_staff:
                return redirect('/admin')
            elif request.user.is_authenticated:
                membergroup =  request.user.erp_user.members_group.all()[0]
                return render(
                    request, 
                    'home.html',
                    {
                        'membergroup':membergroup,
                    }
                )
            else:
                return redirect('login')
        else:
            return redirect('login')
