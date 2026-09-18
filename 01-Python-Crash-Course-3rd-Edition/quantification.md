```Bash
# 切换目录
$ cd \
$ F:
$ cd dev\python-e\examples\image-to-pdf

# 因为要搭配 venv 使用，所以使用 vscode 打开项目
$ code .

# 创建环境
$ py -m venv venv

# 启用环境
$ venv\Scripts\activate.bat

# for MacOS / Linux
$ source venv/bin/activate

# 更新 pip
$ python.exe -m pip install --upgrade pip

# 安装 websocket-client 库
# https://docs.pingcode.com/ask/933530.html
$ pip3 install websocket-client

# for MacOS / Linux
$ python3 -m pip install --upgrade pip

# 将依赖写入 requirements 文件，以便下次使用
$ pip3 freeze > requirements.txt

$ pip3 install -r requirements.txt

# 离开 venv
$ venv\Scripts\deactivate.bat
```

## websocket-client

* [Python 如何安装 websocket](https://docs.pingcode.com/ask/933530.html)
* [websocket-client 1.9.0](https://pypi.org/project/websocket-client/)
* [websocket-client’s documentation](https://websocket-client.readthedocs.io/en/latest/)
* [Connecting through a proxy](https://websocket-client.readthedocs.io/en/latest/examples.html#connecting-through-a-proxy)

## websockets

* [Python 安装 WebSocket](https://geek-docs.com/python/python-ask-answer/289_hk_1710201222.html)

## log

* [logging — Logging facility for Python](https://docs.python.org/3.13/library/logging.html)
