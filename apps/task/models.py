from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Task(models.Model):

	user = models.ForeignKey(User, related_name='ZUOZHE', on_delete=models.CASCADE)
	name = models.CharField('任务', max_length=200, default='1')
	mtime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
	ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

	key_word = models.CharField('关键词', max_length=200, default='')
	target_web = models.CharField('目标网址', max_length=100, default='')

	run_day = models.IntegerField('持续天数', default=0)
	run_time = models.IntegerField('目标次数', default=0)

	count_time = models.IntegerField('统计次数', default=0)
	count = models.IntegerField('统计使用次数', default=0)

	STATUS_CHOICE = (
		(0, "未开始"),
		(1, "开始任务"),
		(2, "暂停任务"),
		(3, "完成"),
	)
	status = models.CharField('状态', choices=STATUS_CHOICE, max_length=50, default=0)

	STATUS_URL = (
		('百度', "https://www.baidu.com"),
		('谷歌', "https://www.baidu.com"),
		('搜狗', "https://www.baidu.com"),
		('360', "https://www.baidu.com"),
	)
	search_url = models.CharField('搜索引擎', max_length=100, default='百度')