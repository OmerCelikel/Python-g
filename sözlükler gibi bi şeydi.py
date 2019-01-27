Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> l  =  [1,19,3,2,1]
>>> 
>>> l[3] # 3 yerine key bişe alıyıruz
2
>>> tel = {'jack': 4098, 'sape': 4139}
>>> 
>>> print (tel['jack'])
4098
>>> print (tel['sape'])
4139
>>> # tanımlamış olduumuz depilkenler geldi
>>> # key değeri artık string ldu mesale jack oldu
>>> 
>>> d = dict([ ('sape',4139), ('guido',4127), ('jack',4098)])
>>> print (d)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> # d nin içine dictoonary attık
>>> #arananı kolaylaştırmak için
>>> 
>>> print a, deg in d.items():
	
SyntaxError: invalid syntax
>>> for a, deg in d.items():
	print(a,deg)

	
sape 4139
guido 4127
jack 4098
>>> print((1, 2, 3)              < (1, 2, 4))
print([1, 2, 3]              < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)           < (1, 2, 4))
print((1, 2)                 < (1, 2, -1))
print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))
SyntaxError: multiple statements found while compiling a single statement
>>> 
KeyboardInterrupt
>>> print((1, 2, 3)              < (1, 2, 4))
True
>>> print([1, 2, 3]              < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)           < (1, 2, 4))
print((1, 2)                 < (1, 2, -1))
print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))
SyntaxError: multiple statements found while compiling a single statement
>>> #üsttekileri unuuuuut
>>> 
>>> print((1, 2, 3)              < (1, 2, 4))
True
>>> print((1, 2, 4)              < (1, 2, 4))
False
>>> print((1, 3, 3)              < (1, 2, 4))
False
>>> print((1, 3, 4)              < (1, 4, 4))
True
>>> print((2, 2, 3)              < (1, 2, 4))
False
>>> #teker teker bakıyor
>>> print('ABC' < 'C' < 'Pascal' < 'Python')
True
>>> #sözlük sıralaaması yaptık
>>> 
>>> print((1, 2, 3, 4)           < (1, 2, 4))
True
>>> # 3. de işi bitirdi daha fazlasına gerek olmadı
>>> 
>>> print((1, 2)                 < (1, 2, -1))
True
>>> # sağdaki fazlalık varsa her zaman büyük
>>> 
>>> print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))
True
>>> # aa ve abc durumunda bulduğu için direk kücüğü söyledi bize
