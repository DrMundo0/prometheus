# 学习测试

def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

# 测试函数名以test_打头，这是pytest的约定
# 在文件所在目录执行pytest命令即可运行单元测试
def test_first_last_name():
    formatted_name = get_formatted_name('janis', 'joplin')
    # 断言是必须的
    assert formatted_name == 'Janis Joplin'

def test_first_last_name2():
    formatted_name = get_formatted_name('janis', 'joplin')
    # 断言是必须的
    assert formatted_name == 'Janis Joplin'

