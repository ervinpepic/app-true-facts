from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from . import views

app_name='blog'

urlpatterns = [
    path('', views.post_list_view, name='home'),
    path('create', views.post_create_view, name='create'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.logout, name='logout'),
    re_path(r'^post/(?P<slug>[\w-]+)/$', views.post_detail_view, name='post_detail'),
	re_path(r'^category/(?P<title>[\w-]+)/$', views.category_detail_view, name='category_detail'),

    

	

 ]