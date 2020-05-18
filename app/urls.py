from django.urls import path
from .views import IndexView, PostDetailView, CategoryListView, TagListView, CategoryPostView, TagPostView, PostsView, SearchPostView


app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='toppage'),
    path('posts/', PostsView.as_view(), name="posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tag/', TagListView.as_view(), name= 'tag_list'),
    path('category/<str:category_slug>/',
         CategoryPostView.as_view(), name='category_post'),
    path('tag/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
    path('search/', SearchPostView.as_view(), name='search_post'),
]