from django.urls import path
from .views import BlogView, BlogDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit')
]
