from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=False)
    date_time = models.DateTimeField(auto_now=True)
    # logged_time
    # logged = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Messages(models.Model):
    text = models.CharField(max_length=200)
    # picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return str(self.user) + ' - ' + str(self.date_time) + ' - ' + self.text
