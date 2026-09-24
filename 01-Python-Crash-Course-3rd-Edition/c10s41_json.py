# 学习JSON模块的使用
from pathlib import Path
import json

if __name__ == "__main__":
    numbers = [ 2, 3, 5, 7, 11, 13 ]
    path = Path('numbers.json')
    # 校验文件是否存在
    print(path.exists())
    # 生成JSON字符串
    contents = json.dumps(numbers)
    path.write_text(contents)

    contents2 = path.read_text()
    numbers2 = json.loads(contents2)
    print(numbers2)
