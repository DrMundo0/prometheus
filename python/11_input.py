# 学习input函数

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 输出多行提示的话可拼接字符串
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print(f"\nHello, {name}")

# 字符串转换为整型
age = input("How old are you?")
age = int(age)
print(age >= 18)

# 取模运算，如果可以被整除则结果为0，不能整除则返回余数
number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
