# 演示向量 v = (2, 1) 的重复相加
import color
from e0218 import length
from draw2d import draw
from patch2d import Arrow, Polygon, Points, Segment, add, dino_vectors

# x轴坐标
vxs = [ 0, 2, 4, 6, 8, 10 ]
# y轴坐标
vys = [ 0, 1, 2, 3, 4, 5 ]
# 将x轴坐标和y轴坐标组合为向量列表
vectors = [ (x, y) for x, y in zip(vxs, vys) ]

# 将向量列表组合为向量对列表
pairs = list(zip(vectors, vectors[1:]))
# 用向量对列表生成箭头列表
arrows = [ Arrow(y, x, color=color.red) for x, y in pairs ]

draw(
    Points(*vectors, color=color.blue),
    *arrows
)
