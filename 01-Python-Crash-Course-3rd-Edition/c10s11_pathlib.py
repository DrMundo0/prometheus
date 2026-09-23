# 学习标准库，如何读文件内容、写入内容

from pathlib import Path
import os

def count_words(path: Path):
    """计算一个文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

if __name__ == "__main__":
    path = Path('01.ipynb')

    try:
    # 读取文件的全部内容
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
        # 提示完错误中断程序，文件都没读到，后面的逻辑没法跑
        os._exit(0)
    else:
        # 去除右侧的空格
        contents = contents.rstrip()
        # 链式调用：method chaining
        # contents = path.read_text().rstrip()
        print(contents)

        # 将文件内容分割为行
        lines = contents.splitlines()
        for line in lines:
            print(line)
            print(len(line))

        # 将内容写入文件
        contents = "I love programming.\n"
        contents += "I love creating new games.\n"
        contents += "I also love working with data.\n"
        path.write_text(contents)

    count_words(path)
