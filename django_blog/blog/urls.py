from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrationView, UserProfileView, PostCreateView, PostDeleteView,PostDetailView, PostListView, PostUpdateView
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView, CommentListView, post_search_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', RegistrationView.as_view(template_name='blog/register.html'), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('posts/', PostListView.as_view(), name='list_posts'),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='viewing_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    # urls for comment
    path('post/<int:pk>/comments', CommentListView.as_view(), name='list_comments'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='create_comment'),
    path('post/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('post/<int:post_id>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    # search url
    path('post/search', post_search_view, name='search')
]


# ["tags/<slug:tag_slug>/", "PostByTagListView.as_view()"]