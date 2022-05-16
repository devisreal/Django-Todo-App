from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Todo
from .forms import AddTodoForm

# Create your views here.


def home_view(request):
   todos = Todo.objects.all()
   context = {
      'todos': todos
   }
   return render(request, 'todo/home.html', context)


def new_todo(request):
   if request.method == "POST":
      form = AddTodoForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('home-view')
   else:
      form = AddTodoForm()

   context = {
       'form': form
   }
   return render(request, 'todo/new_todo.html', context)




def todo_details(request, slug):
   todo = Todo.objects.get(slug=slug)
   context = {
      'todo': todo
   }
   return render(request, 'todo/todo_details.html', context)

def edit_todo(request, slug):
   todo = Todo.objects.get(slug=slug)
   form = AddTodoForm(request.POST or None, instance=todo)
   if form.is_valid():
      form.save()
      return redirect('todo-details', slug=slug)
   context = {
      'form': form,
      'todo': todo
   }
   return render(request, 'todo/edit_todo.html', context)
   
def delete_todo(request, slug):
   todo = Todo.objects.get(slug=slug)
   todo.delete()
   return redirect('home-view')
