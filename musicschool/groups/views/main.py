from musicschool.groups.models import MemberGroup, SchoolRight
from django.shortcuts import redirect


def home_redirect(request):
    try:
        user_information = request.user.user_information
        if request.user.is_staff or request.user.user_information.schoolright_set.first().level == SchoolRight.PROF:
            return redirect('prof-home')
        elif request.user.user_information.schoolright_set.first().level == SchoolRight.STUDENT:
            return redirect('student-home')    
        else:
            return render(request, 'myapp/index.html')
    except:
        return redirect('login')
