from musicschool.libs.logged_view import LoggedProfView, LoggedStudentView
from musicschool.groups.models import MemberGroup, Media, Article
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from musicschool.groups.forms import ArticleForm
from django.shortcuts import get_object_or_404


# Detail 
class ArticleDetailView(LoggedStudentView):
    template_name = "article/home.html"
    
    def get(self, request, article_id):
        article = get_object_or_404(Article, pk=article_id)
        if request.user.is_staff or request.user.user_information.is_prof:
            return render(
                request, 
                'article_detail.html', 
                {
                    'article':article,
                }
            )
        elif request.user.is_authenticated:   
            membergroup =  request.user.members_group.all()[0]
            if article in membergroup.articles.all():
                return render(
                    request, 
                    'article_detail.html', 
                    {
                        'article':article,
                    }
                ) 
        return redirect('login')


# List 
class ArticleListView(LoggedProfView):
    template_name = "prof/article/article_list.html"
    
    def get(self, request):
        articles = Article.objects.all()
        return render(
            request, 
            self.template_name, 
            {
                'articles':articles
            }
        ) 


#Edit - add
class ArticleManageView(LoggedProfView):
    template_name = "prof/article/article_add_edit.html"
    
    def get(self, request, article_id = None):
        if article_id:
            article = get_object_or_404(Article, pk=article_id)
            article_form = ArticleForm(instance=article)
            return render(
                request, 
                self.template_name,
                {
                   'article_form': article_form
                }
            ) 
        else:
            article_form = ArticleForm()
            return render(
                request, 
                self.template_name,
                {
                    'article_form': article_form
                }
            ) 

    def post(self, request, article_id = None):
        if article_id:
            article = get_object_or_404(Article, pk=article_id)
            article_form = ArticleForm(request.POST or None, instance=article)
        else:
            article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('article-list')

#Delete
class ArticleDeleteView(LoggedProfView):            
    def get(self, request, article_id = None):
        article = get_object_or_404(Article, pk=article_id)
        article.delete()
        return redirect('article-list')