import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add, add2, translate
from Fig0221 import multiply
from Fig0224 import subtract
from patch2d import Arrow, Polygon, Points, Segment

# 图2-30：逃命吧！100只恐龙出现
if __name__ == "__main__":
    # 原来列表推导式还可以连起来写
    translations = [ (12 * x, 10 * y) for x in range(-5, 5) for y in range(-5, 5) ]
    # 列表推导式结合函数爆发威力
    dinos = [ Polygon(*translate(t, dino_vectors), color=color.blue) for t in translations]

    draw(*dinos, grid=None, axes=None, origin=None)
