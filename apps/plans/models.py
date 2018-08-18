# -*- coding:utf-8 -*-
from django.db import models
from apps.users.models import UserProfile
# Create your models here.


class Plans(models.Model):

    goal = models.CharField(max_length=70)

    now_status = models.CharField(max_length=100)
    method = models.CharField(max_length=2000)

    author = models.ForeignKey(UserProfile, related_name='goal', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goal
