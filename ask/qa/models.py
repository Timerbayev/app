from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_add')

    def popular(self):
        return self.order_by('-rating')

# Create your models here.
class Question (models.Model):
    object = QuestionManager()
    title = models.CharField(max_length=50)
    text  = models.TextField()
    added_add = models.DateTimeField(blank=True)
    rating  = models.IntegerField(default=0)
    author = models.CharField(max_length=120)
    likes = models.ManyToManyField(User)

class Answer (models.Model):
    text = models.TextField()
    added_add = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question,null=True, on_delete=models.SET_NULL)
    author = models.CharField(max_length=120)
