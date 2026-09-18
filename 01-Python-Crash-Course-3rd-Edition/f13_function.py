# 学习函数

# ------ Fig1 ------
def greet_usr():
    """显示简单的问候语"""
    print("Hello!")

greet_usr()

# ------ Fig2 ------
# username是形参
def greet_usr(username: str):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")

# jesse是实参
greet_usr('jesse')

# ------ Fig3 ------
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# 基于位置实参传递参数，将按顺序一一对应
describe_pet('hamster', 'harry')

# 基于关键字实参传递，参数的顺序随意
describe_pet(animal_type='dog', pet_name='willie')

# ------ Fig4 ------
# 为形参设置默认值，有默认值的形参必须写在参数列表后面
# 默认值不仅能简化函数调用，还能清楚指出函数的典型用法
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='willie')
# 因为pet_name在第一位，调用时也可以简化
describe_pet('willie')
# 覆盖默认值
describe_pet(pet_name='harry', animal_type='hamster')

# ------ Fig5 ------
# 星号写在形参前面表示这个形参的类型是元组，可接收任意数量的参数，toppings是一个元组
def make_pizza(*toppings: tuple[str]):
    """打印顾客点的所有配料"""
    print(f"\n{type(toppings)}, {type(toppings).__name__}, Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepers', 'extra cheese')

# ------ Fig6 ------
# 当函数不止一个可变参数时，固定参数要写在前面
def make_pizza(size, *toppings: tuple[str]):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza(8, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pepers', 'extra cheese')

# ------ Fig7 ------
# 一个星号创建元组，两个星号创建字典，函数里面定义两个字典，将对传入的字典进行扩展
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# 传递方式竟然是直接指定键值名的方式，和前面的灵活传参的方式就对接上了，一种语法，两种作用，妙
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
