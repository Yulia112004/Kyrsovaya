from django.urls import path
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('detail/<slug>/', BlogDetailView.as_view(), name='detail'),
    path('edit/<slug>/', BlogUpdateView.as_view(), name='edit'),
]