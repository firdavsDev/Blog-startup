from django.urls import path

from . import views
urlpatterns = [
    path('url/', views.url,name='url'),
    path('create/', views.create,name='create'),
    path('short/<str:pk>', views.go,name='go'),
]