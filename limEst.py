from math import sqrt
#from pylab import *
#from numpy import *
def f(n):
    return sqrt(n**5+2*n)-sqrt(n**5+1)
#float(((-1)**n)*n^2)/((n+1)**3-(n-1)**3)
#linspace = array([
#figure()

for i in range(5000):
    print("%02d | %.10f | %.10f " % (i, f(i), abs(f(i)-f(i+1))))