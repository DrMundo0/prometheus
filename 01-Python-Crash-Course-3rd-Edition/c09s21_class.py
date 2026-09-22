class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make # 品牌
        self.model = model # 型号
        self.year = year # 生产年份
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

if __name__ == "__main__":
    my_new_car = Car('audi', 'a4', 2024)
    print(my_new_car.get_descriptive_name())
