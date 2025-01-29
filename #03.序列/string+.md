## 字符串
前面提到，字符串也是序列的一种；  
其实，字符串功能类似于元组，也是初始化后无法修改；  
字符串的区别在于元素是字符，而且功能更加丰富；
```py
>>> s='hello'
>>> s[0]
'h'
>>> s[0]='H'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> s='Hello'
>>> s
'Hello'
```

## 常见字符串函数
### `S.find(sub[,start,[end]])`
类似于`L.index()`；  
不过，`S.find()`不限于单个元素，也可以是多个元素组成的字符串，此时返回`sub`字符串的第1个字符的下标；

此外，若没有找到，不会报错，而是返回`-1`；
```py
>>> s='this is a test' 
>>> s.find('a')        
8
>>> s.find('is')
2
>>> s.find('c') 
-1
>>> s.find('is',3)   
5
>>> s.find('is',3,6) 
-1
```

### `S.count(sub[,start,[end]])`
相对于`L.count()`，该函数可以搜寻多个字符以及指定搜索范围；
```py
>>> s='this is a test'
>>> s.count('is') 
2
>>> s.count('is',0,4) 
1
```

### `S.title()` `S.upper()`  `S.lower()`
这些函数只针对于英文字符串；  
`S.title()`返回将**每个单词**的**首字母大写**的字符串；  
`S.upper()`返回**全部大写**的字符串；  
`S.lower()`返回**全部小写**的字符串；
```py
>>> s='hello wORLD'
>>> s.title()
'Hello World'
>>> s.upper()
'HELLO WORLD'
>>> s.lower()
'hello world'
>>>
```

### `S.strip()` `S.lstrip()` `S.rstrip()`
分别返回去除两端、左边、右边**空格**的字符串；
```py
>>> s='  py  '
>>> s.strip()
'py'
>>> s.lstrip() 
'py  '
>>> s.rstrip()  
'  py'
```

### `S.replace(old,new)`
将字符串中所有`old`字符串**替换**为`new`字符串，然后返回（不改变原有字符串）；
```py
>>> s='This is a test'
>>> s.replace('is','IS')
'ThIS IS a test'
>>> s
'This is a test'
```

### `S.join(X)`
将序列`X`里的**元素 合并**为新字符串，之间用字符串`S`做间隔；  
其中X必须是**字符串序列**；
```py
>>> a=['1','3','5','7','9']
>>> ','.join(a)
'1,3,5,7,9'
```

### `S.split([sep])`
将S分割成多个元素，然后组成列表；  
sep为分割标志，如果没有该参数，就不分割，列表中只有1个元素，即该字符串；  
```py
>>> s='1,3,5,7,9'
>>> s.split(',')
['1', '3', '5', '7', '9']
>>> s.split()    
['1,3,5,7,9']
```
