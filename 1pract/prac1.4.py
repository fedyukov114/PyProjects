from math import sin, tan
def f(n):
    if n == 0:
        return(10)
    else:
        return(sin(f(n - 1)) + tan(f(n - 1)) - 30)

print('%.2e' % f(5))