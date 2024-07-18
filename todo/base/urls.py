from django.urls import path

from .views import index, create, edit, delete

app_name = 'base'
urlpatterns = [
    path('', index, name='home'),
    path('create/', create, name='create'),
    path('edit/<int:todo_id>', edit, name='edit'),
    path('delete/<int:todo_id>', delete, name='delete'),
]
