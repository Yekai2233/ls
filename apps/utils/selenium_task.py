# -*-coding:utf-8-*-
from selenium import webdriver
import time
from task.models import Task


class Options(object):

	def __init__(self):
		# 设置 chrome 二进制文件位置
		self._binary_location = ''
		# 添加启动参数
		self._arguments = []
		# 添加扩展应用
		self._extension_files = []
		self._extensions = []
		# 添加实验性质的设置参数
		self._experimental_options = {}
		# 设置调试器地址
		self._debugger_address = None


def get_xpath(driver, sql, count):
	try:
		a = driver.find_elements_by_xpath(sql)
	except Exception as e:
		print('fuck! %s' % e)
	else:
		if a:
			for i in a:
				print(i.text)
				time.sleep(3)
				i.click()
				return 1
		elif count < 4:
			print('nothing get')
			count += 1
			driver.find_element_by_xpath('//a[@class="n" and contains(text(), "下一页")]').click()
			time.sleep(3)
			get_xpath(driver, sql, count)


def selenium_task(kw, target, url):
	options = webdriver.ChromeOptions()
	options.add_argument('lang=zh_CN.UTF-8')
	prefs = {"profile.managed_default_content_settings.images": 2}
	options.add_experimental_option("prefs", prefs)

	driver = webdriver.Chrome(chrome_options=options)
	sql = "//a[@class='c-showurl' and contains(text(),'%s')] | //a[@target='_blank']/span[contains(text(),'%s')]" % (
		target, target)

	driver.get(url)

	driver.find_element_by_id("kw").clear()
	time.sleep(1)
	driver.find_element_by_id("kw").send_keys(kw)
	time.sleep(1)
	driver.find_element_by_id("su").click()
	time.sleep(3)

	count = 0
	c = get_xpath(driver, sql, count)
	return c


def start_selenium():
	task_list = Task.objects.filter(status=False).filter(run_time__gt=0)
	for task in task_list:

		kw = task.key_word
		target = task.target_web
		url = task.search_url
		c = selenium_task(kw, target, url)

		if c:
			task.run_time -= c
			task.save()


