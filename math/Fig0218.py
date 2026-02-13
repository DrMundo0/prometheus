from math import sqrt

def length(v):
    # 根据勾股定理，斜边长度等于两直角边平方和的平方根
    return sqrt(v[0]**2 + v[1]**2)
