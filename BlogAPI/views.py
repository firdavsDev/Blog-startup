# Create your views here.
from django.shortcuts import render
# Create your views here.
from blog.models import Post  #modellarimiz
from .serializers import PostSerializer,UserSerializers #serialasers

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView #apiview
from rest_framework import permissions, serializers #ruxsatlar
#permisons tekshiruv
from .permissions import IsAuthorOrReadOnly #file
from django.contrib.auth import get_user_model

class Postlist(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# User uchun
class UserList(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers

class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers



################################################################# Viewsetda ishlash
from rest_framework.viewsets import ModelViewSet
class PostViewset(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewset(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers