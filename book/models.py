from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):

    title=models.CharField(max_length=50,default='Book')
    desc=models.TextField()
    author=models.CharField(max_length=50,default='author')
    rate=models.FloatField(default=1,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    type=models.TextField()
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
