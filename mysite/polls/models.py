import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Category(models.Model):
    # Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


class News(models.Model):
    # Id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    URL = models.CharField(max_length=255)
    top_image = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




