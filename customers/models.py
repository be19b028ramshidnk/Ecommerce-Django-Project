from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Customer(models.Model):
    LIVE =1
    DELETE =0
    delete_choice =((LIVE,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'customer_profile')
    phone=models.CharField(max_length=15)
    delete_status= models.IntegerField(choices=delete_choice,default= LIVE)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    