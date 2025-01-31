# 函数
Python内置了很多有用的函数，并且可以定义自己的函数。

在交互模式中，使用`help()`可以查看参数对应函数的原型以及用法；
```py
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
```

## 函数的定义
使用`def`定义函数；  
当函数重复定义时，取后面一个定义；
```py
def func(x):
    if(x>0):
        return 1
    elif(x==0):
        return 0
    else:
        return -1
```
该函数用于判断数的正负；

## 函数的调用
在定义函数后可以在后面的程序中调用函数；  
```py
>>> def func(x):
...     if(x>0):
...         return 1
...     elif(x==0):
...         return 0
...     else:
...         return -1
...
>>> func(5)
1
>>> func(-2) 
-1
>>> func(0)
0
```

## 函数的参数
### 默认值参数
在python中，函数的参数可以有默认值；  
这样，在调用函数时如果少写了参数，就会使用默认值，而不是报错；

给参数赋值以让参数有默认值；  
比如下面计算两点之间的距离，如果没有足够数量的参数，就会默认为0；
```py
>>> import math
>>> def dis(x1=0,y1=0,x2=0,y2=0):
...     return math.sqrt((x1-x2)**2+(y1-y2)**2)
...
>>> dis(1,1,2,2)
1.4142135623730951
>>> dis(1,1)     
1.4142135623730951
>>> dis()
0.0
```

使用默认值参数时要注意，函数的参数必须是不可变对象，否则参数的默认值每次都会改变；
```py
>>> def add(l=[]):
...     l.append(1)
...     return l
...
>>> add()   
[1]
>>> add()
[1, 1]
>>> add()
[1, 1, 1]
>>> add()
[1, 1, 1, 1]
```
此时正确做法是将默认值设为`None`，等到它没有传入参数时才将其变成空列表`[]`；
```py
>>> def add(l=None):
...     if(l==None):
...             l=[]
...     l.append(1)
...     return l
...
>>> add()
[1]
>>> add()
[1]
>>> add()
[1]
```

### 可变参数
可变的是参数的数量，如下面一个函数：
```py
>>> def sum(*num):
...     sum=0
...     for i in num:
...         sum+=i
...     return sum
...
>>> sum(1)
1
>>> sum(1,8,9,54,3) 
75
>>> sum()
0
```
这里通过对参数加`*`的方式，使得参数变成了元组里面的元素；  
这时无论是传入多少个参数，甚至不传，都不会出现问题；  

此外，序列无法作为函数参数，但是给序列加上`*`就可以将序列解开为多个元素；
```py
>>> sum(*(1,2,3))
6
```

### 关键字参数
关键字参数在**函数调用**的时候，相对于位置参数而言的；  
位置参数就是常规的调用参数方式，将参数按照位置顺序依次赋值给函数里的参数；  

这样有个坏处，就是参数太多容易搞混位置；  
比如前面的`dis(x1,y1,x2,y2)`函数，`y1`和`x2`的位置就容易搞混；   

而关键字参数则通过指明形参的形式来定向给某参数赋值，无视位置限制；  
还可以搭配默认值参数使用；
```py
>>> import math
>>> def dis(x1=0,y1=0,x2=0,y2=0):
...      return math.sqrt((x1-x2)**2+(y1-y2)**2)    
...
>>> dis(y1=1) 
1.0
>>> dis(x2=3,y2=4)
5.0
```
但是要注意的是，一旦前面使用了关键字参数，后面就不能再使用位置参数；
比如下面的调用，由于前面2个参数是关键字参数，所以后面2个参数不能是位置参数：
```python
>>> dis(y1=3,x1=4,4,5)
  File "<stdin>", line 1
    dis(y1=3,x1=4,4,5)
                     ^
SyntaxError: positional argument follows keyword argument
```
但是在关键字参数前面使用位置参数是不影响的；
```py
>>> dis(1,1,y2=4,x2=3)
3.605551275463989
```

此外，还可以使用关键字参数向函数传入没有的参数，此时需要用`**`来收集成一个**字典**；
```py
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

此时，`name`，`age`以外的关键字参数参数都会被收集进字典`kw`中；  
```py
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```

和可变参数类似，也可以先组装出一个字典，然后，把该字典转换为关键字参数传进去：
```py
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

### 复杂的传参数情况
默认值参数、可变参数、关键字参数相结合可以极大地拓展函数的功能；  
但是，也极大地复杂了函数的理解难度以及参数传入的规则；  
因此在这里展示复杂的传入参数情况；  
```py
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
```

```py
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
```

1. 当参数个数较少时，会优先传给必有参数；
2. 如果还是不够，导致非默认值必有参数没有赋值，则报错；
3. 如果必有的参数（可变参数之前）满足了，剩下的参数都会传给可变参数，而可变参数之后的参数只能通过默认值参数来传；

## 函数的返回值
函数的返回值只有1个，没有返回值指的是返回值为`None`的情况；  
但是，可以通过返回元组的方式返回多个值；  
```py
def twice(x,y):
    return 2*x,2*y
```

```py
>>> twice(2,4) 
(4, 8)
>>> a=twice(2,4) 
>>> a[0]
4
>>> a[1]
8
```
可以看到，返回的其实是一个元组，只是省略了括号；
相应地，也可以通过省略括号的元组来接收返回值；
```py
>>> x,y=twice(2,4)
>>> x
4
>>> y
8
```

