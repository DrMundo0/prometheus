# 第三种，只导入需要的函数并指定别名，原函数名将失效
from f14_module_define import make_pizza as mp

# 用函数别名调用
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green pepers', 'extra cheese')
