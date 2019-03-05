from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from musicschool.groups.views import (
    ArticleDetailView,
    ArticleListView,
    ArticleManageView,
    ArticleDeleteView,
    CategoryListView,
    CategoryManageView,
    CategoryDeleteView,
    home_redirect,
    MediaListView,
    MediaManageView,
    MediaDeleteView,
    MemberGroupListView,
    MemberGroupManageView,
    MemberGroupDeleteView,
    ProfView,
    StudentView,
    RegistrationView,
    UserListView,
    UserManageView,
    UserDeleteView
)

urlpatterns = [
	path('', auth_views.LoginView.as_view(), name="login"),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/register/', RegistrationView.as_view(), name='register'),
    path('home', home_redirect, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),

    ###############################################################
    # student
    path('student/home/', StudentView.as_view(), name='student-home'),
    # prof
    path('prof/home/', ProfView.as_view(),name='prof-home'),

    ###############################################################
    # articles 
    path('article/<int:article_id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/list/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:article_id>/edit/', ArticleManageView.as_view(), name='article-edit'),
    path('article/add/', ArticleManageView.as_view(), name='article-add'),
    path('article/<int:article_id>/del/', ArticleDeleteView.as_view(), name='article-del'),

    ###############################################################
    # user 
    path('user/list/', UserListView.as_view(), name='user-list'),
    path('user/<int:user_id>/edit/', UserManageView.as_view(), name='user-edit'),
    path('user/add/', UserManageView.as_view(), name='user-add'),
    path('user/<int:user_id>/del/', UserDeleteView.as_view(), name='user-del'),

    ##############################################################
    # membergroup
    path('membergroup/list/', MemberGroupListView.as_view(), name='membergroup-list'),
    path('membergroup/<int:member_group_id>/edit/', MemberGroupManageView.as_view(), name='membergroup-edit'),
    path('membergroup/add/', MemberGroupManageView.as_view(), name='membergroup-add'),
    path('membergroup/<int:member_group_id>/del/', MemberGroupDeleteView.as_view(), name='membergroup-del'),

    ###############################################################
    # media 
    path('media/list/', MediaListView.as_view(), name='media-list'),
    path('media/<int:media_id>/edit/', MediaManageView.as_view(), name='media-edit'),
    path('media/add/', MediaManageView.as_view(), name='media-add'),
    path('media/<int:media_id>/del/', MediaDeleteView.as_view(), name='media-del'),

    ###############################################################
    # category 
    path('category/list/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:category_id>/edit/', CategoryManageView.as_view(), name='category-edit'),
    path('category/add/', CategoryManageView.as_view(), name='category-add'),
    path('category/<int:category_id>/del/', CategoryDeleteView.as_view(), name='category-del'),

    ###############################################################
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)