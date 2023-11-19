import math


def f(x):
    return 4 * 1 / math.e ** (x*0.5) - x


def fturev(x):
    return -2 * 1 / math.e ** (x*0.5) - 1


x0 = 2
for i in range(4):
    
    x1 = x0 - f(x0) / fturev(x0)
    x0 = x1

print(x1)

print(f(x1))