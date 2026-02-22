import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add, add2, translate
from Fig0218 import length
from Fig0221 import scale
from Fig0224 import subtract, distance
from Fig0256 import to_cartesian, to_polar, rotate
from patch2d import Arrow, Polygon, Points, Segment
from math import tan, pi, sin, cos, asin, sqrt, acos, atan2
from random import uniform

# 求正多边形的各个顶点的极坐标
def regular_polygon(n):
    # 求多边形的顶点弧度就是平分派的过程，2派是一个圆，2派除以多边形的顶点数就是每一份顶点的弧度，乘以顶点的序号就是每一个顶点的弧度，由此得出每个顶点的极坐标，再传入to_cartesian函数，将极坐标转换为笛卡尔坐标
    return [ to_cartesian((1, 2 * pi / n * k)) for k in range(0, n)]

# 图2-57：一个规则的七边形，其顶点围绕原点均匀分布
if __name__ == "__main__":
    vectors = regular_polygon(7)
    draw(Points(*vectors), Polygon(*vectors))
