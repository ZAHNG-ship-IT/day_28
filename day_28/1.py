#一种简单的方式是使用模块 json 来存储数据
# JSON 数据格式并不是 Python 专用的，这让你能够将以 JSON 格式存储的
# 数据与使用其他编程语言的人共享。这是一种轻量级数据格式，不仅很有用，也易于
# 学习。


# JSON（JavaScript Object Notation）格式最初是为 JavaScript 开发的，但随
# 后成了一种通用的格式，被包括 Python 在内的众多语言采用。

###自己尝试写一个

from pathlib import Path
import json

nums = [1,2,3,4,5,6,7,8,9]

path = Path('nums.json')

contents = json.dumps(nums)

path.write_text(contents)###3json.dumps() 函数接受一个实参，即要转换为 JSON 格式的数据。这个函数返回一
####个字符串，这样你就可将其写入数据文件了：

###读取的话明天再写！！！！！
###自己写的第一个.json文件
