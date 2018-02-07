#! /usr/bin/python
from gevent import monkey;monkey.patch_all()
import gevent
import time


def data_handler(anum,nun):
	print(anum,nun)
	

gevent.joinall([
    gevent.spawn(data_handler,1,2000),
    gevent.spawn(data_handler,2001,5000),
    gevent.spawn(data_handler,5001,8000),
    gevent.spawn(data_handler,8001,10000),
])

