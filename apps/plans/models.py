# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Plans(models.Model):

    goal = models.CharField(max_length=70, default='money')

    now_status = models.CharField(max_length=2000,default='no money')
    future_status = models.CharField(max_length=2000, default='a lot of money')
    mtime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    author = models.ForeignKey(User, related_name='goal', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-mtime', '-ctime']
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goal


class Process(models.Model):

    process_name = models.CharField(max_length=70)
    mtime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    plan_id = models.ForeignKey(Plans, related_name='process', on_delete=models.CASCADE)

    TIME_CHOICES = (
        ('long_time', '长期执行'),
        ('period_time', '阶段执行')
    )

    time_choice = models.CharField(verbose_name='任务时间属性', max_length=20, choices=TIME_CHOICES, default='long_time')
    start_time = models.DateTimeField(verbose_name='开始日期')
    end_time = models.DateTimeField(verbose_name='结束日期')

    content = models.CharField(max_length=2000)


class ProcessScore(models.Model):
    STATUS_CHOICES = (
        ('complete', '完成'),
        ('do', '执行'),
        ('try', '尝试'),
        ('forget', '遗忘')
    )

    process_status = models.CharField(verbose_name='任务时间属性', max_length=8, choices=STATUS_CHOICES, default='forget')
    process_score = models.IntegerField(verbose_name='分数', default=0)
    process_id = models.ForeignKey(Process, related_name='score', on_delete=models.CASCADE)