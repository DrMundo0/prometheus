from draw2d import draw
from patch import Arrow, Polygon, Points, Segment

draw(
    # 横坐标从-10开始，不包含11，到10结束，使用列表推导式生成一个横坐标不变，纵坐标是横坐标的平方的向量组，绘制这些点，这将绘制一个符合方程 y = x^2 的点阵集合
    Points(*[(x, x**2) for x in range(-10, 11)]),
    # 定义网格线，默认网格线是 (1, 1) 纵向的线太密集，纵向改为每十个单位话一条线
    grid=(1, 10),
    # 关闭横轴、纵轴的同比例开关
    nice_aspect_ratio=False
)
