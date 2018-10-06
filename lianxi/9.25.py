Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t=([1,2,3],[4,5,6],[7,8,9])
>>> t(0,0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    t(0,0)
TypeError: 'tuple' object is not callable
>>> t[0,0]TypeError: 'tuple' object is not callable
SyntaxError: invalid syntax
>>> t[0,0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t[0,0]
TypeError: tuple indices must be integers or slices, not tuple
>>> t=[[1,2,3],[4,5,6],[7,8,9]]
>>> t[0,0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t[0,0]
TypeError: list indices must be integers or slices, not tuple
>>> t=([1,2,3],[4,5,6],[7,8,9])
>>> t[0][0]
1
>>> t[0]
[1, 2, 3]
>>> t[1]
[4, 5, 6]
>>> t[][0]
SyntaxError: invalid syntax
>>> t(0)(0)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t(0)(0)
TypeError: 'tuple' object is not callable
>>> t[1][1]
5
>>> t[:][0]
[1, 2, 3]
>>> list[t[0][0],t[1][0],t[2][0]]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list[t[0][0],t[1][0],t[2][0]]
TypeError: 'type' object is not subscriptable
>>> t[2][0]
7
>>> list(t[0][0],t[1][0],t[2][0])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(t[0][0],t[1][0],t[2][0])
TypeError: list() takes at most 1 argument (3 given)
>>> t[0:]
([1, 2, 3], [4, 5, 6], [7, 8, 9])
>>> t[0:][0]
[1, 2, 3]
>>> t[1:][0]
[4, 5, 6]
>>> t[1:]
([4, 5, 6], [7, 8, 9])
>>> t[1:][1]
[7, 8, 9]
>>> t=[[1,2,3],[4,5,6],[7,8,9]]
>>> t[2][2]
9
>>> t[2][1]
8
>>> t[1]
[4, 5, 6]
>>> t[1]*2
[4, 5, 6, 4, 5, 6]
>>> t[1]+t[0]
[4, 5, 6, 1, 2, 3]
>>> [t[0][0],t[1][0],t[2][0]]
[1, 4, 7]
>>> t[2][1]*t[1][2]
48
>>> a=[]
>>> a[i][k]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a[i][k]
NameError: name 'i' is not defined
>>> a=array([1,2,3],[4,5,6],[7,8,9])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a=array([1,2,3],[4,5,6],[7,8,9])
NameError: name 'array' is not defined
>>> from numpy import *
>>> a=array([1,2,3],[4,5,6],[7,8,9])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a=array([1,2,3],[4,5,6],[7,8,9])
ValueError: only 2 non-keyword arguments accepted
>>> a=array([[1,2,3],[4,5,6],[7,8,9]])
>>> a[2][2]
9
>>> a[][0]
SyntaxError: invalid syntax
>>> a[:][0]
array([1, 2, 3])
>>> a[0]
array([1, 2, 3])
>>> a[0]*a[1]
array([ 4, 10, 18])
>>> t[0]*t[1]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t[0]*t[1]
TypeError: can't multiply sequence by non-int of type 'list'
>>> t[0]+t[1]
[1, 2, 3, 4, 5, 6]
>>> a[0]+a[1]
array([5, 7, 9])
>>> m=mat([[1,2,3],[4,5,6],[7,8,9]])
>>> m
matrix([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
>>> m[0]*m[1]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    m[0]*m[1]
  File "C:\Users\Danling\AppData\Local\Programs\Python\Python35\lib\site-packages\numpy\matrixlib\defmatrix.py", line 309, in __mul__
    return N.dot(self, asmatrix(other))
ValueError: shapes (1,3) and (1,3) not aligned: 3 (dim 1) != 1 (dim 0)
>>> m[0]*m[1].T
matrix([[32]])
>>> m[0,]
matrix([[1, 2, 3]])
>>> m[,0]
SyntaxError: invalid syntax
>>> m[:,1:3]
matrix([[2, 3],
        [5, 6],
        [8, 9]])
>>> m[:,0:1]
matrix([[1],
        [4],
        [7]])
>>> m[:,0]
matrix([[1],
        [4],
        [7]])
>>> a[:][1]
array([4, 5, 6])
>>> a[:][0:1]
array([[1, 2, 3]])
>>> 
