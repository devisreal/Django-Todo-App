from django.urls import path
from .views import home_view, edit_todo, new_todo, todo_details, delete_todo

urlpatterns = [
   path('', home_view, name="home-view"),
   path('new_todo/', new_todo, name="new-todo"),
   path('edit_todo/<slug:slug>', edit_todo, name="edit-todo"),
   path('todo_details/<slug:slug>', todo_details, name="todo-details"),
   path('delete_todo/<slug:slug>', delete_todo, name="delete-todo"),
]
