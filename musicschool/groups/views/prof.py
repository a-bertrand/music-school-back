from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from  musicschool.groups.models import MemberGroup, Media, Article

class ProfView(TemplateView):
    template_name = 'prof/home.html'

    def get(self, request):
        if request.user:
            if request.user.is_staff:
                return redirect('/admin')
            elif request.user.is_authenticated:
                try:
                    membergroup =  request.user.members_group.all()[0]
                except:
                    membergroup = None
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
