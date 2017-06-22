# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#分类表
class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
#标签表
class Tag(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
#文章表

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
    def increase_view(self):
        self.views += 1
        self.save(update_fields=['views'])



