from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True)
    following = models.ManyToManyField(
        'self', 
        through='Subscription', 
        related_name='followers', 
        symmetrical=False
    )

    def __str__(self):
        return self.username

# Промежуточная модель для подписок (дает больше контроля в будущем)
class Subscription(models.Model):
    user = models.ForeignKey(User, on_local='user', related_name='rel_from_set', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_local='author', related_name='rel_to_set', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'], name='unique_relationships')
        ]