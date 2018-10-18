#js=介绍=intro/introduction
#https://docs.python.org/3/tutorial/introduction.html

'''原文
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
'''

垃圾=1
文本="# 因为井号在双引号里面，所以这一行不是注释"


''' 3.1. Using Python as a Calculator
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
'''

1.6 == 8/5 #和py2不同，斜杠除法只返回浮点数 //我就是不用直译，直译是总是返回

'''
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
'''

5 is 17 // 3 # 整除
2 == 17 % 3 # 取余

'''
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
'''

25 == 5**2 # 指数为2

'''
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
'''
宽=20; 高=5*9; 面积=宽*高 

'''
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
'''
# 这段traceback说的是：NameError/ 变量n没有定义
'''
>>> 4 * 3.75 - 1
14.0
'''
#这里演示的是优先级的问题。注：APL没有算术优先级


'''
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
'''
税=1/1;价格=1;价格*税
上一次结果=lambda:_
价格*上一次结果()
四舍五入=round
四舍五入(上一次结果(),2) #保留两位小数

