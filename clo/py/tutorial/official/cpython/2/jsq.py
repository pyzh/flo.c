'''
jsq=解释器=interpreter
https://docs.python.org/3/tutorial/interpreter.html

说明：if这种简单的词就不翻了
'''
# 代码片段1
"""
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
"""

# 片段一/汉化
原文='Be careful not to fall off!'
翻译='小心别掉下来。'  # https://fanyi.baidu.com/#en/zh/Be%20careful%20not%20to%20fall%20off

语句=翻译; 输出=print
真的,假的 =True,False

世界是平的？ = 真的

世界是平的 = 真的 if 世界是平的？ else 假的

# if 世界是平的: 输出(语句)

如果 = lambda x,是,否: 是 if x else 否

略 = None # 省略-> pass
若 = lambda 真,则: 则 if 真 else 略

若 (世界是平的, 则=输出(语句)) # 注：不记得这句是不是真的能运行，感觉会报错。回头测试一下

  
# -*- coding: encoding -*-

"""
For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:

# -*- coding: cp1252 -*-
"""
