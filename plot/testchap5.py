__author__='yangyang'
import numpy as np

def f(x):
	return 2

def fv(x):
	if isinstance(x, (float, int)):
		return 2
	elif isinstance(x, np.ndarray):
		return np.zeros(x.shape, x.dtype)+2
	else:
		raise TypeError\
			('x must be int, float or ndarray, not %s'%type(x))

x=np.linspace(1,10,50)

t=np.linspace(1,30,30).reshape(5,6)

print t
print '\n'
print np.ix_([2,4]),np.ix_([3,4])
print '\n'
print t[np.ix_([2,4]),np.ix_([3,4])]
print '\n'
print t[np.ix_([2,4])]
print '\n'
print t[np.ix_([3,4])]
print '\n'

print t[:,np.ix_([3,4])]
print '\n'
