from django.urls import path


from . import views
urlpatterns = [
    path('tarjima/', views.tarjima,name='tarjima')
]