#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 #  @file       cron.py
 #  @brief      定时任务
 #  @version    1.0.0
 #  @author     LindenTao(lindentao@qq.com)
 #  @date       2018/1/8 下午3:20
 #  @history    <author>    <time>    <desc>

"""

from apscheduler.schedulers.background import BackgroundScheduler
from utils.selenium_task import start_selenium

def main():
    """ 计划任务处理的主函数 """
    sched = BackgroundScheduler()
    sched.daemonic = False
    sched.misfire_grace_time = 180
    # sched.add_job(sendemail.deal_email, 'cron', second='*/5')
    # sched.add_job(rate.update_rate, 'cron', hour='0')
    # sched.add_job(order.change_order_status, 'cron', hour='5')
    # sched.add_job(order.run_countdown, 'cron', hour='*/1')
    # sched.add_job(renew_company_city_list, 'cron', hour='4')
    sched.add_job(start_selenium, 'cron', minute='*/1')

    # sched.add_job(rate.record_rate, 'cron', hour='*/3')
	#
    # sched.add_job(sand_supplier, 'cron', hour='7') # 早上7点执行
    # sched.add_job(sand_supplier, 'cron', hour='19') # 晚上七点执行


    try:
        # 启动定时任务
        sched.start()
    except (KeyboardInterrupt, SystemExit) as e:
        sched.shutdown()