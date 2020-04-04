from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null= True)
    date_event = models.DateTimeField(verbose_name='Date of Event')
    date_creation = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Para evento pertencer ao usuário
    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.title  #retorna o nome do titulo do evento