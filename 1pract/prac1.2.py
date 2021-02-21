from math import*

def f(x):
    if x<50:
        return(pow(e, (x**5)/16) - x**8)
    elif x >= 50 and x < 78:
        return(tan(log1p(x)) + 93*x**3 - 52)
    elif x >= 78 and x < 176:
        return(pow((x**4 - (x**7/93) + 5),6) + 33*x**3)
    elif x >= 176:
        return((x**8/27) + x**5 + 36)

print('%.2e' % f(55))
