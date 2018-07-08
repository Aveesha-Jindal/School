from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    author = models.ManyToManyField(Author,related_name='Authors')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    issued = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=250)
    book = models.ManyToManyField(Book, related_name='SBooks')
    issue_date = models.DateField(default=timezone.now().date())
    book_count = models.IntegerField(default=0)
    due_date = models.DateField(default=timezone.now().date() + timedelta(days=20))

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=250)
    book = models.ManyToManyField(Book, related_name='TtBooks')
    issue_date = models.DateField(default=timezone.now().date())
    book_count = models.IntegerField(default=0)
    due_date = models.DateField(default=timezone.now().date() + timedelta(days=20))

    def __str__(self):
        return self.name


