from django.contrib import admin
from .models import Todo

# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
   list_display = ("todo_title",)
   search_fields = ("todo_title",)
   list_filter = ("is_completed",)
