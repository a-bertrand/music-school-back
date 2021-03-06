from django.views.generic.base import View
from musicschool.libs.logged_view import LoggedProfView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from musicschool.groups.forms import MediaForm
from musicschool.groups.models import Media
from django.shortcuts import get_object_or_404
from django.contrib import messages



class MediaListView(LoggedProfView):
    template_name = "prof/media/media_list.html"

    def get(self, request):
        medias = Media.objects.all()
        return render(
            request, 
            self.template_name,
             {'medias': medias}
        )


class MediaManageView(LoggedProfView):
    template_name = "prof/media/media_add_edit.html"

    def get(self, request, media_id = None):
        if media_id:
            media = get_object_or_404(Media, pk=media_id)
            media_form = MediaForm(instance=media)
            return render(
                request, 
                self.template_name,
                {
                   'media_form': media_form
                }
            ) 
        else:
            media_form = MediaForm()
            return render(
                request, 
                self.template_name,
                {
                    'media_form': media_form
                }
            ) 

    def post(self, request, media_id = None):
        if media_id:
            media = get_object_or_404(Media, pk=media_id)
            media_form = MediaForm(request.POST or None, request.FILES or None, instance=media)
        else:
            media_form = MediaForm(request.POST, request.FILES)
        if media_form.is_valid():
            media_form.save()
            messages.success(request, "Mise à jour validé")
        return render(
            request, 
            self.template_name,
            {
                'media_form': media_form
            }
        ) 


class MediaDeleteView(LoggedProfView):
    def get(self, request, media_id = None):
        if media_id:
            media = get_object_or_404(Media, pk=media_id)
            media.delete()
        return redirect('media-list')