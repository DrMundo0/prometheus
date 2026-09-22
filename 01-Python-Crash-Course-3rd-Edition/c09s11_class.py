# 学习类的定义
# 类的首字母大写
class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

if __name__ == "__main__":
    # Python中实例化对象不需要写new
    my_dog = Dog('Willie', 6)
    print(f"My dog's name is {my_dog.name.title()}.")
    print(f"My dog is {my_dog.age} years old.")
    my_dog.sit()
    my_dog.roll_over()

    your_dog = Dog('Gala', 3)
    print(f"\nYour dog's name is {your_dog.name.title()}")
    print(f"Your dog is {your_dog.age} years old.")
    your_dog.sit()
    your_dog.roll_over()
