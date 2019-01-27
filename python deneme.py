Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = [1,2,3]
>>> m = [ [1,3,5,6] , [3,4,5] , l]
>>> 
>>> print (m)
[[1, 3, 5, 6], [3, 4, 5], [1, 2, 3]]
>>> l [1] = 100
>>> print (m)
[[1, 3, 5, 6], [3, 4, 5], [1, 100, 3]]
>>> # birden fazla boyutu tutmak için
>>> #l yi değiştirdiğimde m de değişiyor
>>> k = [[[ 1 , 2 ,3 ] , [2,3,4] ] , [[1, 2,3] , [1,1,1]] , [[1,1]]]
>>> 
>>> print (k)
[[[1, 2, 3], [2, 3, 4]], [[1, 2, 3], [1, 1, 1]], [[1, 1]]]
>>> l[1] = 2
>>> print (m)
[[1, 3, 5, 6], [3, 4, 5], [1, 2, 3]]
>>> mt [[ row [i]  for  row in m] for i in range(3)]
SyntaxError: invalid syntax
>>> mt = [[row[i]  for row in m] for i in range(3)]
>>> print (mt)
[[1, 3, 1], [3, 4, 2], [5, 5, 3]]
>>> m = [ [1,3,5] , [3,4,5] , l ]
>>> mt = [[row[i]  for row in m] for i in range(3)]
>>> print (mt)
[[1, 3, 1], [3, 4, 2], [5, 5, 3]]
>>> # for gibi ondan ona alıyor 1. nin 1 cisi 2.nin 1. si gibi...
>>> print(len(mt[1]))
3
>>> 
>>> print(len(mt[1]))
3
>>> del(k[1])
>>> print(k)
[[[1, 2, 3], [2, 3, 4]], [[1, 1]]]
>>> a = [1,2,3]
>>> t = (1,2,3)
>>> 
>>> print(l)
[1, 2, 3]
>>> print(a)
[1, 2, 3]
>>> print(t)
(1, 2, 3)
>>> print(l)
[1, 2, 3]
>>> l[2]= 10
>>> print(l)
[1, 2, 10]
>>> # elemanı 10 yaptık
>>> t[2] = 10
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    t[2] = 10
TypeError: 'tuple' object does not support item assignment
>>> print (t)
(1, 2, 3)
>>> # t yi değiştiremedik içerik değiştirilemez
>>> # ram de sakladı , değiştiremedik
>>> 
>>> x , y , z = t
>>> print (x)
1
>>> print (z)
3
>>> # x 1 y 2 z 3 oldu
>>> z = 10
>>> t = (x , y , z)
>>> print (t)
(1, 2, 10)
>>> # değiştirebildik
>>> # garip...
>>> 
