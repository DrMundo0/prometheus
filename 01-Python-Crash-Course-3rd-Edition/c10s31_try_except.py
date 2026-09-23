# 学习异常处理

try:
    # 将引发除数不能为零的异常，ZeroDivisionError: division by zero
    print(5 / 0)
except ZeroDivisionError:
    # 打印错误提示
    print("You can't divide by zero!")
    # 或者静默处理
    pass
else:
    print("Success")
