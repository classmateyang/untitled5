__author__='yangyang'
import numpy as np


#using np.where to vectorize
def Nv(x):
	cond1=x < 0
	cond2=np.logical_and(0<=x,x<1)
	cond3=np.logical_and(1<=x,x<2)
	cond4=x >= 2
	r=np.zeros(len(x))
	r=np.where(cond1, 0., r)
	r=np.where(cond2, x, r)
	r=np.where(cond3, 2-x, r)
	r=np.where(cond4, 0., r)
	return r
#using boolen indexing to vectorize


def Nv2(x):
	cond1=x < 0
	cond2=np.logical_and(0 <= x, x < 1)
	cond3=np.logical_and(1 <= x, x < 2)
	cond4=x >= 2
	r=np.zeros(len(x))
	r[cond1] =0.
	r[cond2] =x[cond2]
	r[cond3] =2-x[cond3]
	r[cond4] =0.
	return r

x=np.linspace(-10,10,40)

print Nv(x)
print Nv2(x)
