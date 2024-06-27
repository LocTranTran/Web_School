from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('',views.base, name = 'base'),
    path('home',views.home, name = 'home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('introduce/', views.introduce, name='introduce'),
]