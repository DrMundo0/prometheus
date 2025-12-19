# 演示列表的用法
# https://jupyter.org/try-jupyter/lab/

# 列表中可以包含不同类型的成员
list0 = [ 27, 1453, "Roman", "Empire" ]

# 索引从0开始，所以2会取到第3个元素
list0[2]

# 列表是动态的，可修改的，修改某个成员值的方式非常直观
list0[1] = "Senate"

# 向列表的末尾添加一个元素
list0.append("Roman")

# Python 支持负数索引，将从结尾开始算，结尾第一个元素的下标是-1，以此类推
list0[-1]

# 翻转列表中的内容
# 第一个-1表示从末尾开始
# 第二个参数为空表示从末尾到开始
# 第三个参数是步长，-1步长表示步长是1，但是方向是反向
list0[-1::-1]

# 计算某个元素出现的次数
list0.count("Roman")

# 查找某个元素出现的下标
list0.index("Roman")

# 反转列表中的元素
list0.reverse()

# 通过 __sizeof__() 函数查看列表所占的内存空间，单位字节
# 列表通过预先分配内存来提高操作效率
list0.__sizeof__()

# -m timeit 可精确测量小段 Python 代码的执行时间
!python3 -m timeit 'x=(1,2,3,4,5,6)'

import timeit

code = "x=[1,2,3,4,5,6]"
print(timeit.timeit(stmt=code, number=20000000))

keys = [x for x in range(0, 100000)]
vals = [x for x in range(200000, 300000)]
list0 = list(zip(keys, vals))
