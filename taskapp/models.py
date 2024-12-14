from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
    
class Task(models.Model):
    PENDING = 'P'
    IN_PROGRESS = 'IP'
    COMPLETED = 'C'
    
    STATUS_CHOICE =[
        (PENDING , 'pending'),
        (IN_PROGRESS , 'in Progress'),
        (COMPLETED , 'completed')
    ]
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null= True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICE,default=PENDING)
    complete = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
