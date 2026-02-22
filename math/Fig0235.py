import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add, add2, translate
from Fig0218 import length
from Fig0221 import scale
from Fig0224 import subtract, distance
from patch2d import Arrow, Polygon, Points, Segment
from math import tan, pi, sin, cos, asin, sqrt, acos, atan2
from random import uniform

# 将极坐标转换为笛卡尔坐标
def to_cartesian(polar_vector):
    # 极坐标元组第一个标量是斜边长，第二个标量是角度
    length, angle = polar_vector[0], polar_vector[1]
    # 正弦sin等于角的对边与斜边的比值
    # 余弦cos等于角的邻边与斜边的比值
    # 所以横坐标就是斜边长乘以角的余弦，纵坐标就是斜边长乘以角的正弦
    return (length * cos(angle), length * sin(angle))

# 将笛卡尔坐标转换为极坐标
def to_polar(vector):
    x, y = vector[0], vector[1]
    # 利用反正切函数根据横坐标和纵坐标得到角度
    angle = atan2(y, x)
    # 利用勾股定理得到斜边的长，斜边的长和角度组成极坐标
    return (length(vector), angle)

# 将任意个向量旋转一定的角度
def rotate(angle, vectors):
    polar = [ to_polar(v) for v in vectors ]
    rotated_polar = [ (l, a + angle) for l, a in polar ]
    rotated = [ to_cartesian(p) for p in rotated_polar ]
    return rotated

# 图2-56：恐龙的旋转和平移
if __name__ == "__main__":
    vs = translate((8, 8), rotate(5 * pi / 3, dino_vectors))
    draw(
        Points(*dino_vectors),
        Polygon(*dino_vectors),
        Points(*vs),
        Polygon(*vs, color=color.red)
    )
