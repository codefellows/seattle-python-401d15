from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    rank = models.IntegerField(default=100)
    priority_eater = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
