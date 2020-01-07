from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    title = models.CharField(verbose_name='Название', max_length=100)
    text = models.TextField(verbose_name='Задача')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    performer = models.CharField(verbose_name='Исполнитель', max_length=25, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
