## 类型转换
虽然前面提到python是动态语言，变量的类型不固定，但是不同类型的变量还是**无法进行运算**的；  
因此类型转换还是十分有必要的；
```python
>>> a=input()
9
>>> a
'9'
>>> int(a)   
9
>>> b=5
>>> a+b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> int(a)+b
14
```
注意：`int()`会直接将字符去掉引号，而不是转换为其`UTF-8`值；  
这也就意味着，不是数字的字符串在python中将**无法进行**类型转换；

### 类型转换函数
类型转换是通过函数实现的，并不是运算符；  
类型转换可能有**不止一个**参数；  
下面是一些常见的类型转换函数；

#### `bool()`
根据参数的逻辑值将其转换为对应的布尔值；
```py
>>> bool(2) 
True
>>> bool(-1) 
True
>>> bool(0) 
False
>>> bool('a') 
True
```

#### `int()` `float()` `complex()` `str()`
将传入的参数转换为对应数据类型的值；
```py
>>> int(3.0)
3
>>> float(3)
3.0
>>> complex(1,2)
1+2j
>>> str(123)
'123'
```

#### `bin()` `oct()` `hex()`
将整数转换为2、8、16进制的**字符串**；
```py
>>> bin(31)
'0b11111'
>>> oct(31)    
'0o37'
>>> hex(31) 
'0x1f'
```