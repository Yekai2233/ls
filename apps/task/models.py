from django.db import models

# Create your models here.


class Task(models.Model):
	
	name = models.CharField('任务', max_length=2000, default='1')
	mtime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
	ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

	key_word = models.CharField('关键词', max_length=20, default='')
	target_web = models.CharField('目标网址', max_length=100, default='')
	run_time = models.IntegerField('目标次数', default=0)
	count_time = models.IntegerField('统计次数', default=0)

	count = models.IntegerField('统计使用次数', default=0)
	status = models.BooleanField('状态', default=False)

	search_url = models.CharField('搜索引擎', max_length=50, default='https://www.baidu.com')