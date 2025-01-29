## 元组
元组和列表大部分相同，只是元组一旦初始化，元素便不可修改，除非重新初始化；  
因此列表的一些内容，包括增删、修改元素及其相关函数都不能使用；
```py
>>> a=(1,3,5,7,9)
>>> a[0]=2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> a.append(11)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> a=(2,3,5,7,9)
>>> a
(2, 3, 5, 7, 9)
```

## 元组的初始化
为了和列表区分，元组用小括号`()`表示；
```py
a=(1,3,5,7,9)
```
但是，要定义一个只有1个元素的tuple，如果你这么定义：
```py
>>> a = (1)
>>> a
1
```
定义的不是元组，而是`1`**这个数**！  
这是因为括号`()`既可以表示tuple，又可以表示数学公式中的小括号，这就产生了**歧义**；  
因此，Python规定，这种情况下，按小括号进行**计算**，**计算结果**自然是`1`。

所以，只有1个元素的tuple定义时**必须**加一个逗号`,`，来**消除歧义**：
```py
>>> t = (1,)
>>> t
(1,)
```
Python在显示只有1个元素的tuple时，也会加一个逗号`,`，以免你误解成数学计算意义上的括号。

## 元组和列表的嵌套
当元组里面有列表元素时，列表元素可变，其它不可变；  
当列表里面有元组元素时，元组元素不可变，其它可变；
```py
>>> a=(1,3,5,[7,9])
>>> a[3][0]=8 
>>> a
(1, 3, 5, [8, 9])
```

```py
>>> a=[1,3,5,(7,9)] 
>>> a[4][0]=8
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```