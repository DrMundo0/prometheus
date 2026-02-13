from draw2d import draw
from patch2d import Arrow, Polygon, Points, Segment

# 练习2.2：在平面上画出点 (2, -2) 和与之对应的箭头
# 图2-10：表示(2, -2)的点和箭头
if __name__ == "__main__":
    vectors = [ (0, 0), (2, -2) ]

    draw(
        # Points 函数至少需要两个向量，只传一个 [ (2, -2) ] 会报错
        Points(*vectors),
        Arrow((2, -2), (0, 0))
    )
