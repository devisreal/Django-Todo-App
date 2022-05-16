from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

from django.db import models

# Create your models here.
class Todo(models.Model):
   todo_title = models.CharField(max_length=150, unique=True)
   todo_text = models.TextField() 
   is_completed = models.BooleanField(default=False)     
   slug = models.SlugField(null=True)

   class Meta: 
      ordering = ('-id',)

   def __str__(self):
      return self.todo_title

   def save(self, *args, **kwargs):
      self.slug = slugify(self.todo_title)
      super().save(*args, **kwargs)
   