__author__='yangyang'
import numpy as np



def Nv(x):
	cond1=x < 0
	cond2=np.logical_and(0<=x,x<1)
	cond3=np.logical_and(1<=x,x<2)
	cond4=x >= 2

	r=np.where(cond1, 0., 0.)
	r=np.where(cond2, x, r)
	r=np.where(cond3, 2-x, r)
	r=np.where(cond4, 0., r)
	return r





x=np.linspace(-4,5,20)

print x
print type(x)
print Nv(x)

