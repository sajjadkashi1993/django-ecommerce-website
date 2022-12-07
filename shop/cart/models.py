from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel

# Create your models here.

User = get_user_model()



class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    
