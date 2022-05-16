from django import forms
from .models import Todo

class AddTodoForm(forms.ModelForm):
   todo_title = forms.CharField(
      label='', 
      widget=forms.TextInput(
         attrs={"placeholder": "Todo Title", "id": "text-title"}
      )
   )
   todo_text = forms.Textarea(
      attrs={'class': 'mt-5'}
   )
   is_completed = forms.BooleanField(
      required=False,      
   )

   class Meta:
      model = Todo
      fields = ("todo_title", "todo_text", "is_completed")
