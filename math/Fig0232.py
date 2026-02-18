import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add, add2, translate
from Fig0221 import scale
from Fig0224 import subtract
from patch2d import Arrow, Polygon, Points, Segment
from random import uniform

# 图2-32：在给定约束条件下r*z+s*v可能出现的位置
if __name__ == "__main__":
    u = (-1, 1)
    v = (1, 1)

    def random_r():
        # 平均分布函数
        return uniform(-3, 3)
    
    def random_s():
        return uniform(-1, 1)
    
    possibilities = [ add(scale(u, random_r()), scale(v, random_s())) for i in range(0, 500) ]

    draw(Points(*possibilities))
