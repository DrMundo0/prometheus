import color
from draw2d import draw
from Fig0207 import dino_vectors
from Fig0213 import add
from patch2d import Arrow, Polygon, Points, Segment

def multiply(a, factor):
    return (a[0] * factor, a[1] * factor)

# 图2-21：标量乘法就是将向量的两个分量按同一系数缩放
if __name__ == "__main__":
    a1 = (6, 0)
    b1 = (0, 4)
    c1 = add(a1, b1)

    factor = 1.5
    a2 = multiply(a1, factor)
    b2 = multiply(b1, factor)
    c2 = multiply(c1, factor)

    vectors = [ a1, b1, c1, a2, b2, c2 ]
    
    draw(
        Points(*vectors),
        Arrow(a1, color=color.blue),
        Arrow(c1, a1, color=color.green),
        Arrow(c1, color=color.red),
        Arrow(a2, color=color.blue),
        Arrow(c2, a2, color=color.green),
        Arrow(c2, color=color.red)
    )
