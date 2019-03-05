from django.views.generic import View
from musicschool.groups.models import SchoolRight

# school/3/login


class LoggedView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(LoggedView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('login')


class LoggedProfView(LoggedView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_information.schoolright_set.first().level == SchoolRight.PROF:
            return super(LoggedProfView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('login')


class LoggedStudentView(LoggedView):
    def dispatch(self, request, *args,  **kwargs):
        if request.user.is_authenticated:
            return super(LoggedStudentView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('login')
