from draw2d import draw
from patch2d import Arrow, Polygon, Points, Segment

# 练习2.5：当x坐标在-10到10的范围内，使用draw函数绘制表示向量(x, x**2)的点
# 图2-12：y=x^2上的点
if __name__ == "__main__":
    draw(
        # 横坐标从-10开始，不包含11，到10结束，使用列表推导式生成一个横坐标逐个加一，纵坐标是横坐标的平方的向量组，绘制这些点，这将绘制一个符合方程 y = x^2 的点阵集合
        Points(*[(x, x**2) for x in range(-10, 11)]),
        # 定义网格线，默认网格线是 (1, 1) 纵向的线太密集，纵向改为每十个单位话一条线
        grid=(1, 10),
        # 关闭横轴、纵轴的同比例开关
        nice_aspect_ratio=False
    )
