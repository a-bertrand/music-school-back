from django.views.generic.base import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from musicschool.groups.forms import MemberGroupForm
from musicschool.groups.models import MemberGroup
from django.shortcuts import get_object_or_404


class MemberGroupListView(View):
    template_name = "prof/MemberGroup/MemberGroup_list.html"

    def get(self, request):
        membergroups = MemberGroup.objects.all()
        return render(
            request, 
            self.template_name,
             {'membergroups': membergroups}
        )


class MemberGroupManageView(View):
    template_name = "prof/MemberGroup/MemberGroup_add_edit.html"

    def get(self, request, member_group_id = None):
        if member_group_id:
            member_group = get_object_or_404(MemberGroup, pk=member_group_id)
            member_group_form = MemberGroupForm(instance=member_group)
            return render(
                request, 
                self.template_name,
                {
                   'member_group_form':member_group_form
                }
            ) 
        else:
            member_group_form = MemberGroupForm()
            return render(
                request, 
                self.template_name,
                {
                    'member_group_form': member_group_form
                }
            ) 

    def post(self, request, member_group_id = None):
        if member_group_id:
            member_group = get_object_or_404(MemberGroup, pk=member_group_id)
            member_group_form = MemberGroupForm(request.POST or None, request.FILES or None, instance=member_group)
        else:
            member_group_form = MemberGroupForm(request.POST, request.FILES)
        if member_group_form.is_valid():
            member_group_form.save()
            return redirect('MemberGroup-list')


class MemberGroupDeleteView(View):
    pass