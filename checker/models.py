from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    name=models.CharField(max_length=20)
    status=models.BooleanField(default=False)
    


class ToDo(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)