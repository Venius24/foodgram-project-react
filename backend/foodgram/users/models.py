from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True) # Обязательно unique=True
    
    USERNAME_FIELD = 'email' # Теперь Django будет считать почту логином
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']   
    
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True)
    following = models.ManyToManyField(
        'self', 
        through='Subscription', 
        related_name='following_lists', 
        symmetrical=False
    )

    def __str__(self):
        return self.username

class Subscription(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='subscriptions'
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='subscribers'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'], name='unique_relationships')
        ]