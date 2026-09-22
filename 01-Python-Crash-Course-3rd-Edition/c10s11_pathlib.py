# 学习标准库，如何读文件内容

from pathlib import Path

if __name__ == "__main__":
    path = Path('note.md')
    # 读取文件的全部内容
    contents = path.read_text()
    # 去除右侧的空格
    contents = contents.rstrip()
    # 链式调用：method chaining
    # contents = path.read_text().rstrip()
    print(contents)
