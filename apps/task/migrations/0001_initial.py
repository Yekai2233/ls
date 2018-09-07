# Generated by Django 2.0.2 on 2018-09-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='1', max_length=2000, verbose_name='任务')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('key_word', models.CharField(default='', max_length=20, verbose_name='关键词')),
                ('target_web', models.CharField(default='', max_length=100, verbose_name='目标网址')),
                ('run_time', models.IntegerField(default=0, verbose_name='目标次数')),
                ('count_time', models.IntegerField(default=0, verbose_name='统计次数')),
                ('count', models.IntegerField(default=0, verbose_name='统计使用次数')),
            ],
        ),
    ]
