from musicschool.libs.logged_view import LoggedProfView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from musicschool.groups.forms import CategoryForm
from musicschool.groups.models import Category
from django.shortcuts import get_object_or_404
from django.contrib import messages


class CategoryListView(LoggedProfView):
    template_name = "prof/category/category_list.html"

    def get(self, request):
        categories = Category.objects.all()
        return render(
            request, 
            self.template_name,
             {'categories': categories}
        )


class CategoryManageView(LoggedProfView):
    template_name = "prof/category/category_add_edit.html"

    def get(self, request, category_id = None):
        if category_id:
            category = get_object_or_404(Category, pk=media_id)
            category_form = CategoryForm(instance=media)
            return render(
                request, 
                self.template_name,
                {
                   'category_form': category_form
                }
            ) 
        else:
            category_form = CategoryForm()
            return render(
                request, 
                self.template_name,
                {
                    'category_form': category_form
                }
            ) 

    def post(self, request, category_id = None):
        if category_id:
            category = get_object_or_404(Category, pk=media_id)
            category_form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
        else:
            category_form = CategoryForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Mise à jour validé")
        return redirect('category-list')


class CategoryDeleteView(LoggedProfView):
    def get(self, request, category_id = None):
        if category_id:
            category = get_object_or_404(Category, pk=media_id)
            category.delete()
        return redirect('category-list')