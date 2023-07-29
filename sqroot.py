import math

def sqroot(num):
    if num <0:
        num=num*-1
        a=math.isqrt(num)
        return str(a)+"i"
    a=math.isqrt(num)
    return a
