#!/usr/bin/env python

def count(wrapped):
	def inner(*args,**kwargs):
		inner.counter += 1
		return wrapped(*args, **kwargs)

	inner.counter = 0
	return inner

@count
def my_func():
	pass

my_func()
my_func()
my_func()
print my_func.counter
