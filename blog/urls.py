from django.urls import path
from . import views

from .views import PostListView, PostDetailView,PostCreateView, PostUpdateView , PostDeleteView, UserPostListView, addPhoto,LikeView #viewslarni kuchirib olamiz
    
urlpatterns = [
    # path('', views.home, name='blog-home'),
    
    path('', PostListView.as_view(), name='blog-home'),
    path('post/', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #itpro
    path('about/', views.about, name='blog-about'),
    #crud
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('add/',views.addPhoto, name='add'),

    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    #filter
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    #like
    path('like/<int:pk>',LikeView,name='like_post'),
    #pdf
    path('post_pdf',views.post_pdf,name='post-pdf')

]

