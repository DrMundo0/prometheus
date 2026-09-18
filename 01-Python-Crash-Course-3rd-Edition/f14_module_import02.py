# 第二种，只导入需要的函数
from f14_module_define import make_pizza

# 调用时就可以省略模块名
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pepers', 'extra cheese')
