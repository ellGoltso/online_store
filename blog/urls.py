from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView


app_name = BlogConfig.name

urlpatterns = [
    path('blog/', PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog/new/', PostCreateView.as_view(), name='post_create'),
    path('blog/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]