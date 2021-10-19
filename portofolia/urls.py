from django.urls import path
from . import views

urlpatterns = [
    path('contact_email/', views.contact, name="contact_email"),
    path('', views.home, name="portfolio"),
]