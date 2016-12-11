#!/usr/bin/env python

def shout(wrap):
	def inner(*args, **kwargs):
		print('Before')
		ret = wrap(*args, **kwargs)
		print('After')
		return ret
	return inner

@shout
def myfunc():
	print('such wow!')

myfunc()
