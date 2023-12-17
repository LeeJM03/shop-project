from django.db import models

# Create your models here.
class Member(models.Model) :
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=128)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'member'
        verbose_name_plural = "members"

    def __str__(self):
        return self.username