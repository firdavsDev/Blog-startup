from django.urls import path

#views import qilish
from . import views

urlpatterns = [
    path('todo/',views.index, name="todo"),
    path('update_todo/<str:pk>/',views.updateTask,name='update_todo'),
    path('delete_todo/<str:pk>/',views.deleteTask,name='delete_todo'),
]