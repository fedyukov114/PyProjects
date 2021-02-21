from math import fabs, tan, sqrt

def f(x):
    return(fabs(31*x**3) - tan(x) + x + 39*x**5 + sqrt(x**3 + ((x**2)/74)-62))

print('%.2e' % f(42))