#!/usr/bin/env python

def func_timer(func):
	def f(*args, **kwargs):
		import time
		start = time.time()
		results = func(*args, **kwargs)
		print "Elaspsed ", (time.time() -start)
		return results
	return f

@func_timer
def sleepy(msg, sleep=1.0):
	import time
	time.sleep(sleep)
	print msg

sleepy("Hi",1.5)
