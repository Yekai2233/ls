# -*-coding:utf-8-*-
from selenium import webdriver
import time
# from task.models import Task
from random_useragent import get_useragent, get_fake_keyword
from get_ip import get_ip_response
import random


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


# 随机长时间
def sleep_long_time():
	all_choice = (1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.2, 3.4, 3.6, 3.8, 4, 5)
	t = random.choice(all_choice)
	time.sleep(t)


# 下移
def scroll_down(driver):
	driver.execute_script(""" 
		(function () { 
			var y = document.body.scrollTop; 
			var step = 30; 
			window.scroll(0, y); 
			function f() { 
				if (y < document.body.scrollHeight) { 
					y += step; 
					window.scroll(0, y); 
					setTimeout(f, 50); 
				}
				else { 
					window.scroll(0, y); 
					document.title += "scroll-done"; 
				} 
			} 
			setTimeout(f, 1000); 
		})(); 
		""")


# 上移
def scroll_up(driver):
	driver.execute_script(""" 
		(function () { 
			var y = 2000; 
			var step = 80; 
			window.scroll(0, y); 
			function f() { 
				if (y > 180) { 
					y -= step; 
					window.scroll(document.body.scrollHeight, y); 
					setTimeout(f, 50); 
				}
				else { 
					window.scroll(document.body.scrollHeight, 0); 
					document.title += "scroll-done"; 
				} 
			} 
			setTimeout(f, 1000); 
		})(); 
		""")


# 搜索框点击
def click_work(driver, word):

	driver.find_element_by_id("kw").clear()
	sleep_long_time()
	driver.find_element_by_id("kw").send_keys(word)
	sleep_long_time()
	driver.find_element_by_id("su").click()


# 切换窗口
def switch_window(driver, fake):
	# 获取当前窗口句柄
	now_handle = driver.current_window_handle

	# 获取所有窗口句柄
	all_handles = driver.window_handles
	if random.randint(1, 3) == 1:
		for handle in all_handles:
			if handle != now_handle:
				# 输出待选择的窗口句柄
				driver.switch_to_window(handle)
				sleep_long_time()
				scroll_down(driver)
				sleep_long_time()
				driver.refresh()
				sleep_long_time()
				# 具体操作
				driver.close()  # 关闭当前窗口

		# 输出主窗口句柄
		sleep_long_time()
		driver.switch_to_window(now_handle)  # 返回主窗口

	else:
		driver.close()
		for handle in all_handles:
			driver.switch_to_window(handle)
			sleep_long_time()
			scroll_down(driver)
			sleep_long_time()
			driver.refresh()
			sleep_long_time()



# 假动作
def fake_work(driver):
	sql2 = "//a[@class='c-showurl'] | //a[@target='_blank']/span"
	fake = get_fake_keyword()
	while fake:

		print(fake)
		now_word = fake.pop()
		click_work(driver, now_word)
		sleep_long_time()
		scroll_down(driver)
		sleep_long_time()
		scroll_up(driver)
		sleep_long_time()

		# 随机随机是否进入下一页
		if random.randint(1, 3) == 1:
			targetElem = driver.find_element_by_xpath('//a[@class="n" and contains(text(), "下一页")]')
			driver.execute_script("arguments[0].scrollIntoView();", targetElem)

		# 随机随机是否选取元素点击进入
		if random.randint(1, 4) != 1:
			fake_clicks = driver.find_elements_by_xpath(sql2)
			click = random.choice(fake_clicks)
			click.click()
			sleep_long_time()
			switch_window(driver, fake)
			sleep_long_time()

	time.sleep(50)


# 主要任务目标
def get_xpath(driver, target, count):
	sql = "//a[@class='c-showurl' and contains(text(),'%s')] | //a[@target\
			='_blank']/span[contains(text(),'%s')]" % (target, target)
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

				time.sleep(5)
				driver.close()

				time.sleep(5)
				#return 1
		elif count < 50:
			print('nothing get')
			count += 1
			targetElem = driver.find_element_by_xpath('//a[@class="n" and contains(text(), "下一页")]')
			driver.execute_script("arguments[0].scrollIntoView();", targetElem)
			targetElem.click()
			time.sleep(3)
			get_xpath(driver, sql, count)


def selenium_task(kw, target, url):
	options = webdriver.ChromeOptions()
	prefs = {"profile.managed_default_content_settings.images": 2}
	options.add_experimental_option("prefs", prefs)
	args = get_useragent()
	# args += ("no-sandbox", "window-size=1904x1500")  # , "disable-gpu"  "headless",
	for arg in args:
		print(arg)
		options.add_argument(arg)

	driver = webdriver.Chrome(chrome_options=options)

	driver.set_page_load_timeout(30)
	driver.get(url)
	sleep_long_time()
	fake_work(driver)

	click_work(driver, kw)

	count = 0
	get_xpath(driver, target, count)


	return t
def start_selenium():
	task_list = Task.objects.filter(status=False).filter(run_day__gt=0)
	for task in task_list:

		kw = task.key_word
		target = task.target_web
		url = task.search_url
		c = selenium_task(kw, target, url)

		if c:
			task.run_time -= c
			task.save()


selenium_task('净水器代理批发', 'www.ouces.com', 'https://www.baidu.com')
