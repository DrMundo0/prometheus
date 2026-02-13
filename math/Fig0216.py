import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add
from patch2d import Arrow, Polygon, Points, Segment

# 图2-16：原始恐龙（蓝色）和平移后的副本（红色）。将每一个点和向量(-1.5, -2.5)相加，让恐龙向左下方移动
if __name__ == "__main__":
    # add((-1.5, -2.5), v) for v in dino_vectors 是一个列表推导式
    # 由两部分构成，先看后面，for v in dino_vectors 循环取出数组 dino_vectors 中的每一个向量
    # 再看前面的部分，add((-1.5, -2.5), v) 是对循环取出的每一个向量要做的操作，这个表达式中的 v 就是后面循环语句中指代每个向量所使用的 v
    # 这两部分加起来之后，将会返回21个都加了 (-1.5, -2.5) 的向量，用中括号括起来，让他们组成一个新的向量数组
    # dino_vectors 中每个向量都加 (-1.5, -2.5) 相当于左移 1.5，再下移 2.5
    dino_vectors2 = [ add((-1.5, -2.5), v) for v in dino_vectors ]

    draw(
        Points(*dino_vectors, color=color.blue),
        Polygon(*dino_vectors, color=color.blue),
        Points(*dino_vectors2, color=color.red),
        Polygon(*dino_vectors2, color=color.red)
    )

    # 画出每个点的移动矢量，用黑色箭头表示
    arraws = [ Arrow(tip, tail, color=color.black) for (tip, tail) in zip(dino_vectors2, dino_vectors) ]

    draw(
        Points(*dino_vectors, color=color.blue),
        Polygon(*dino_vectors, color=color.blue),
        Points(*dino_vectors2, color=color.red),
        Polygon(*dino_vectors2, color=color.red),
        *arraws
    )
