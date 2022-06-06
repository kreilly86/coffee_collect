from . import views
from django.urls import path

urlpatterns = [
    path('index.html', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='producer'),
    path('coffee.html', views.PostList.as_view(), name='coffee'),
    path('about.html', views.PostList.as_view(), name='about'),
    path('join.html', views.PostList.as_view(), name='join'),
]
