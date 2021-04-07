# -*- coding: utf-8 -*-

import logging
from datetime import datetime

now = datetime.now() # current date and time
year = now.strftime("%Y")
print("year:", year)
month = now.strftime("%m")
print("month:", month)
day = now.strftime("%d")
print("day:", day)
time = now.strftime("%H:%M:%S")
print("time:", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)


# debug < info < warning < error < critical
# =========================================
log_filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")

logging.basicConfig(level = logging.INFO,
	format = '[%(asctime)s %(levelname)-8s] %(message)s',
	datefmt = '%Y%m%d %H:%M:%S',
	filename = log_filename,
	)

if __name__ == "__main__":
	logging.debug('debug')
	logging.info('info')
	logging.warning('warning')
	logging.error('error')
	logging.critical('critical')