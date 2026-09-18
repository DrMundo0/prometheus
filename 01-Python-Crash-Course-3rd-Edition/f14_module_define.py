# 模块的文件名必须以字母开头，不能以数字开头
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")
