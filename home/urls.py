from django.urls import path
from . import views
from .views import (PostListView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView,
                    api_data, 
                    )

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<str:slug>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('chuck-norris-jokes/', views.api_data, name='chuck-norris-jokes'),
]
