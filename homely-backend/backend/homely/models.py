from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, to_field="username")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="gallery", default = "gallery/default.jpg") 
    activity_type = models.CharField(max_length = 20, null = True)
    
    def _str_(self):
        return self.title
        
class PersonalTodo(models.Model):
    title = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, to_field="username", related_name="ptodo_set")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.title
