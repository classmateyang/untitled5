__author__='yangyang'
from scitools.std import sin, sqrt, linspace, ndgrid, mesh

def f(x,y):
	return sin(sqrt(x**2+y**2))

x=y=linspace(-5,5,100)
xv,yv=ndgrid(x,y)
z=f(xv,yv)
mesh(xv,yv,z)
raw_input('press enter to exit')