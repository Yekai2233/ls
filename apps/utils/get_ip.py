import requests
from lxml import etree
import threading
import random

lock = threading.Lock()


def get_ip_response(url):
	proxies_list = []
	headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
		}
	response = requests.get(url=url, headers=headers)
	selector = etree.HTML(response.text)
	tr = selector.xpath('//tr')[:80]
	L = []
	for i in range(81):
		if tr:
			t = threading.Thread(target=check_ip, args=(tr, proxies_list, headers,))
			t.start()
			L.append(t)

	for t in L:
		t.join()
	return proxies_list


def check_ip(tr, proxies_list, headers):
	lock.acquire()
	td = tr.pop()
	lock.release()
	td = td.xpath('./td/text()')
	try:
		proxies = {td[4]: td[0] + ':' + td[1]}
		requests.get(url='http://hotels.ctrip.com/hotel/hangzhou17#ctm_ref=ctr_hp_sb_lst', headers=headers, proxies=proxies, timeout=5)
	except:
		print('connect failed')
	else:

		if len(td) == 7:
			proxies_dict = {td[4].lower(): td[0] + ':' + td[1]}
		else:
			proxies_dict = {td[3].lower(): td[0] + ':' + td[1]}
		proxies_list.append(proxies_dict)


if __name__ == '__main__':

	get_ip_response()
