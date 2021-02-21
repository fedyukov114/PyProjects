from math import cos, e

def f1(n, m):
    res1 = 0
    res2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res1 = (e**j - (i**5/16))

    for i in range(1, n + 1):
        res2 = (cos(i) - 76*i**5)
    
    return(90*res1 - res2)


print('%.2e' % f1(51, 27))