# 定义各种2d形状

import color
from math import sqrt

# 箭头
class Arrow():
    def __init__(self, tip, tail=(0, 0), color=color.red):
        self.tip = tip
        self.tail = tail
        self.color = color

# 多边形
class Polygon():
    def __init__(self, *vertices, color=color.blue, fill=None, alpha=0.4):
        self.vertices = vertices
        self.color = color
        self.fill = fill
        self.alpha = alpha

# 点
class Points():
    def __init__(self, *vetors, color=color.black):
        self.vectors = list(vetors)
        self.color = color

# 线段
# start_point：起始向量
# end_point：结束向量
class Segment():
    def __init__(self, start_point, end_point, color=color.blue):
        self.start_point = start_point
        self.end_point = end_point
        self.color = color

# 定义向量加法运算函数，向量的加法就是组成向量的两个成员分别相加，组成新的向量
# 加法可以理解为向量的移动，先向 x 轴的左或者右移动，再向 y 轴的上或者下移动
def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

# 向量加法的第二个版本，支持传入任意多个向量，使用了列表推导式
def add2(*vs):
    return (sum([v[0] for v in vs]), sum([v[1] for v in vs]))
