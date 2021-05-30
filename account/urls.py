from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostUpdateView, PostListView, UserPostListView

urlpatterns=[
	path('', PostListView.as_view(), name='home'),
	path('post/new/', views.create_post, name='post-create'),
	path('post/<int:pk>/', views.post_detail, name='post-detail'),
	path('like/', views.like, name='post-like'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
	path('search_posts/', views.search_posts, name='search_posts'),
	path('user_posts/<str:username>', UserPostListView.as_view(), name='user-posts'),
	path('about', views.about, name='about'),
	path('contact', views.contact, name='contact'),
	path('contact_process', views.contact_process, name='contact_process'),
	path('privacypolicy', views.privacypolicy, name='privacypolicy'),
	path('sitemap.xml', views.sitemap, name='sitemap'),

]