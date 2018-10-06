Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
NameError: name 'Iterable' is not defined
>>> from collections import Iterable, Iterator
>>> print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
Iterable? [1, 2, 3]: True
>>> print('Iterable? \'abc\':', isinstance('abc', Iterable))
Iterable? 'abc': True
>>> print('Iterable? 123:', isinstance(123, Iterable))
Iterable? 123: False
>>> def g():
    yield 1
    yield 2
    yield 3

    
>>> print('Iterable? g():', isinstance(g(), Iterable))
Iterable? g(): True
>>> print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator)）
      
SyntaxError: invalid character in identifier
>>> print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
Iterator? [1, 2, 3]: False
>>> print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
Iterator? iter([1, 2, 3]): True
>>> print('Iterator? \'abc\':', isinstance('abc', Iterator))
Iterator? 'abc': False
>>> print('Iterator? 123:', isinstance(123, Iterator))
Iterator? 123: False
>>> print('Iterator? g():', isinstance(g(), Iterator))
Iterator? g(): True
>>> print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> for x in [1, 2, 3, 4, 5]:
	print(x)

	
1
2
3
4
5
>>> for x in iter([1, 2, 3, 4, 5]):
    print(x)

    
1
2
3
4
5
>>> print('next():')
next():
>>> it = iter([1, 2, 3, 4, 5])
>>> print(next(it))
1
>>> print(next(it))
2
>>> print(next(it))
3
>>> print(next(it))
4
>>> print(next(it))
5
>>> print(next(it))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(next(it))
StopIteration
>>> it = iter([1, 2, 3, 4, 5])
>>> for x in it():
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    for x in it():
TypeError: 'list_iterator' object is not callable
>>> for x in it:
	print(x)

	
1
2
3
4
5
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> print('iter key:',d)
iter key: {'a': 1, 'c': 3, 'b': 2}
>>> for k in d.keys():
	print('key:',k)

	
key: a
key: c
key: b
>>> print('iter value:', d)
iter value: {'a': 1, 'c': 3, 'b': 2}
>>> for v in d.values():
	print('value:',v)

	
value: 1
value: 3
value: 2
>>> print('iter item:', d)
iter item: {'a': 1, 'c': 3, 'b': 2}
>>> for k, v in d.items():
	print('items:',k,v)

	
items: a 1
items: c 3
items: b 2
>>> print('iter enumerate([\'A\', \'B\', \'C\']')
iter enumerate(['A', 'B', 'C']
>>> for i, value in enumerate(['A', 'B', 'C']):
	print(i,value)

	
0 A
1 B
2 C
>>> 
KeyboardInterrupt
>>> print('iter [(1, 1), (2, 4), (3, 9)]:')
iter [(1, 1), (2, 4), (3, 9)]:
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x,y)

	
1 1
2 4
3 9
>>> abs
<built-in function abs>
>>> x=abs(-100)
>>> x
100
>>> f=abs
>>> f(-100)
100
>>> abs=10
>>> bas(-10)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    bas(-10)
NameError: name 'bas' is not defined
>>> def add(x,y,f):
	return f(x)+f(y)

>>> add(-5,6,abs)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    add(-5,6,abs)
  File "<pyshell#69>", line 2, in add
    return f(x)+f(y)
TypeError: 'int' object is not callable
>>> add(-5,6,abs)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    add(-5,6,abs)
  File "<pyshell#69>", line 2, in add
    return f(x)+f(y)
TypeError: 'int' object is not callable
>>> def add(x,y,f):
	return f(x)+f(y)

>>> add(-5,6,abs)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    add(-5,6,abs)
  File "<pyshell#74>", line 2, in add
    return f(x)+f(y)
TypeError: 'int' object is not callable
>>> 
KeyboardInterrupt
>>> def f(x)
SyntaxError: invalid syntax
>>> def f(x);
SyntaxError: invalid syntax
>>> def f(x0:
      return x*x
      
SyntaxError: invalid syntax
>>>  def f(x):
	 
SyntaxError: unexpected indent
>>> def f(x):
	return x*x

>>> r=map(f,[1,2,3,4,5,6,7,8])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64]
>>> def f(x):
	return x*x

>>> f2)
SyntaxError: invalid syntax
>>> f(2)
4
>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> def f(x):
	return x*x

>>> reduce(f,[1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    reduce(f,[1,2,3,4])
NameError: name 'reduce' is not defined
>>> from functools import reduce
>>> def f(x):
	return x*x

>>> reduce(f,[1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    reduce(f,[1,2,3,4])
TypeError: f() takes 1 positional argument but 2 were given
>>> from functools import reduce
>>> def add(x,y):
	return x+y

>>> reduce(add,[1,3,5,7,9,11])
36
>>> from functools import reduce
>>> def fn(x,y):
	return x*10+y

>>> return(fn,[1,3,5,7,9])
SyntaxError: 'return' outside function
>>> reduce (fn,[1,3,5,7,9])
13579
>>> 
KeyboardInterrupt
>>> from functools import reduce
>>> def fn(x,y):
	return x*10+y

>>> def char2nm(x):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'9':9}[s]

>>> r=map(char2num, '13579')
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    r=map(char2num, '13579')
NameError: name 'char2num' is not defined
>>> map(char2num, '13579')
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    map(char2num, '13579')
NameError: name 'char2num' is not defined
>>> reduce(fn, map(char2num, '13579'))
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    reduce(fn, map(char2num, '13579'))
NameError: name 'char2num' is not defined
>>> 
>>> 
KeyboardInterrupt
>>> from functools import reduce
>>> def fn(x, y):
	return x * 10 + y

>>> def char2num(s):
	 return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

	
>>> reduce(fn, map(char2num, '13579'))
13579
>>> r=map(char2num, '13579')
>>> list(r)
[1, 3, 5, 7, 9]
>>> return reduce(fn, map(char2num, s))
SyntaxError: 'return' outside function
>>> def str2int(s):


	jdyt

	
>>> from functools import reduce
>>> def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		 return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
		return reduce(fn, map(char2num, s))
	
SyntaxError: unindent does not match any outer indentation level
>>> from functools import reduce
>>> def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))

>>> 
>>> str2int({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9})
7645318290
>>> str2int(0,1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    str2int(0,1,2,3,4)
TypeError: str2int() takes 1 positional argument but 5 were given
>>> str2int([1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    str2int([1,2,3,4,5])
  File "<pyshell#155>", line 6, in str2int
    return reduce(fn,map(char2num,s))
  File "<pyshell#155>", line 5, in char2num
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
KeyError: 1
>>> 
>>> def normalize(name):
	fg

	
>>> 
>>> lower(A)
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    lower(A)
NameError: name 'lower' is not defined
>>> lower('A')
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    lower('A')
NameError: name 'lower' is not defined
>>> print 'A'.isupper()
SyntaxError: invalid syntax
>>> print 'A'.isupper()
SyntaxError: invalid syntax
>>> print 'A'.isupper()
SyntaxError: invalid syntax
>>> 'A'.lower()
'a'
>>> A.lower()
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    A.lower()
NameError: name 'A' is not defined
>>> s = 'hEllo pYthon'
>>> print s.capitalize()
SyntaxError: invalid syntax
>>> print s.title()
SyntaxError: invalid syntax
>>> print 'hEllo pYthon'.title()
SyntaxError: invalid syntax
>>> print s.upper()
SyntaxError: invalid syntax
>>> print (s.upper())
HELLO PYTHON
>>> print (s.capitalize())
Hello python
>>> print (s.title())
Hello Python
>>> print ('A'.isupper())
True
>>> print('a'.isupper())
False
>>> help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

>>> map(lambda x: x+1,[1,2,3,4])
<map object at 0x00000283BCCF7DA0>
>>> list(x)
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    list(x)
TypeError: 'int' object is not iterable
>>> lambda
SyntaxError: invalid syntax
>>> lambda()
SyntaxError: invalid syntax
>>> map(lambda x,y: x+y,[1,2,3,4],(10,20,30,40))
<map object at 0x00000283BCCF7E80>
>>> print(map(lambda x,y: x+y,[1,2,3,4],(10,20,30,40)))
<map object at 0x00000283BCD0A5C0>
>>> list(map(lambda x,y: x+y,[1,2,3,4],(10,20,30,40)))
[11, 22, 33, 44]
>>> list(map(lambda x,y: x+y if y else x+10,[1,2,3,4,5],(1,2,3,4)))
[2, 4, 6, 8]
>>> list(map(lambda x,y: x+y if y else x+10,[1,2,3,4,5],(1,2,3,4)))
[2, 4, 6, 8]
>>> list(map(lambda x,y: x+y if y true else x+10,[1,2,3,4,5],(1,2,3,4)))
SyntaxError: invalid syntax
>>> list(map(lambda x,y: if y x+y  else x+10,[1,2,3,4,5],(1,2,3,4)))
SyntaxError: invalid syntax
>>> list(map(None,[1,2,3,4,5],(1,2)))
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    list(map(None,[1,2,3,4,5],(1,2)))
TypeError: 'NoneType' object is not callable
>>> map(None,[1,2,3,4,5],(1,2))
<map object at 0x00000283BCCF7D30>
>>> list(<map object at 0x00000283BCCF7D30>)
SyntaxError: invalid syntax
>>> list{map(None,[1,2,3,4,5],(1,2))}
SyntaxError: invalid syntax
>>> list[map(None,[1,2,3,4,5],(1,2))]
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    list[map(None,[1,2,3,4,5],(1,2))]
TypeError: 'type' object is not subscriptable
>>> names = ['Alice','Jerry','Bob','Barbar']
>>> map(len,names)
<map object at 0x00000283BA7CFD30>
>>> list(map(len,names))
[5, 5, 3, 6]
>>> m = [1,4,7]
>>> n=[2,5,8]
>>> map(None,m,n)
<map object at 0x00000283BCCF7DA0>
>>> list(map(None,m,n))
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    list(map(None,m,n))
TypeError: 'NoneType' object is not callable
>>> map(operator.gt,a,b)
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    map(operator.gt,a,b)
NameError: name 'operator' is not defined
>>> L1 = ['adam', 'LISA', 'barT']
>>> def normalize(name):
	
KeyboardInterrupt
>>> def normalize(name):
	return(name.capitalize())

>>> 
KeyboardInterrupt
>>> L1 = ['adam', 'LISA', 'barT']
>>> L2 = list(map(normalize, L1))
>>> print(L2)
['Adam', 'Lisa', 'Bart']
>>> 
>>> from functools import reduce
>>> def prod(L)
SyntaxError: invalid syntax
>>> def prod(L):
	def fn(x,y):
		return x*y
	return reduce(fn,map(prod,L))

>>> print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
  File "<pyshell#228>", line 4, in prod
    return reduce(fn,map(prod,L))
  File "<pyshell#228>", line 4, in prod
    return reduce(fn,map(prod,L))
TypeError: 'int' object is not iterable
>>> def prod(L):
	def fn(x,y):
		return x*y
	return reduce(fn,map(L))

>>> print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
  File "<pyshell#235>", line 4, in prod
    return reduce(fn,map(L))
TypeError: map() must have at least two arguments.
>>> def prod(L):
	def fn(x,y):
		return x*y
	return reduce(fn,map(L,[ ]))

>>> print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
  File "<pyshell#241>", line 4, in prod
    return reduce(fn,map(L,[ ]))
TypeError: reduce() of empty sequence with no initial value
>>> def prod(L):
	def fn(x,y):
		return x*y
	return reduce(fn,map(L,[3,5,7,9]))

>>> print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
  File "<pyshell#247>", line 4, in prod
    return reduce(fn,map(L,[3,5,7,9]))
TypeError: 'list' object is not callable
>>> def fn(x,y):
	return x*y

>>> reduce(fn,[3,5,7,9])
945
>>> def prod(L):
	def fn(x,y):
		return x*y
	return reduce(fn,L)

>>> print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
3 * 5 * 7 * 9 = 945
>>> 
