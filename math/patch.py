# 定义各种形状

import color

# 箭头
class Arrow():
    def __init__(self, tip, tail=(0,0), color=color.red):
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
