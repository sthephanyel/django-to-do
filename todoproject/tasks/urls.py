from django.urls import path
from . import views

urlpatterns = [
    path('helloword/', views.helloWorld),
    # todas as tasks
    path('', views.taskList, name='task-list'),
    # task especifica
    path('task/<int:id>', views.taskView, name='task-view'),
    # nova task
    path('newtask/', views.newTask, name='new-task'),
    # editando uma task existente
    path('edit/<int:id>', views.editTask, name='edit-task'),
    # excluindo
    path('delete/<int:id>', views.deleteTask, name='delete-task'),
    # status
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]
