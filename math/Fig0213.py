import color
from draw2d import draw
from patch2d import Arrow, Polygon, Points, Segment

# 定义向量加法运算函数，向量的加法就是组成向量的两个成员分别相加，组成新的向量
# 加法可以理解为向量的移动，先向 x 轴的左或者右移动，再向 y 轴的上或者下移动
def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

# 图2-13：绘制出(4, 3)和(-1, 1)的向量和
if __name__ == "__main__":
    # 三个点，演示向量的加法
    a = (-1, 1)
    b = (4, 3)
    c = add(a, b)
    vectors = [ a, b, c ]

    draw(
        Points(*vectors),
        # 第一个向量
        Arrow(a),
        # 第二个向量
        Arrow(b),
        # 这两个向量相加之后的向量
        Arrow(c, color=color.blue),
        # 用箭头表示两个向量相加的首尾加法
        Arrow(c, b, color=color.green)
    )
