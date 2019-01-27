Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> l = [1,2,3] # liste
>>> t = (1,2,3) # kayt
>>> k = {1,2,3} # kumeler set
>>> print(k)
{1, 2, 3}
>>> # kümede sıra önemli değil , tekrar olmaz
>>> l = [1,2,3,1,2,1,3]
>>> k = {1,2,3,1,2,1,3}
>>> print (l)
[1, 2, 3, 1, 2, 1, 3]
>>> print(k)
{1, 2, 3}
>>> # kümede tekrar olmaz !
>>> k2 = set(l) # set kümeye çevirir
>>> k3 = set ([1,2,3,1,32,3])
>>> print (k2)
{1, 2, 3}
>>> print(k3)
{32, 1, 2, 3}
>>> #kümeye çevirdi set
>>> k4 = set ('omeroguzcelıkel')
>>> k5 = set ('mefunıversıtesıbılgısayarmuhendıslıgı')
>>> print (k4)
{'u', 'o', 'z', 'c', 'g', 'l', 'k', 'ı', 'e', 'r', 'm'}
>>> print(k5)
{'ı', 'y', 'd', 'u', 'b', 't', 'h', 'a', 'l', 's', 'n', 'v', 'g', 'f', 'e', 'r', 'm'}
>>> # aynıları almadı cunku KUME
>>> # sıranın onemı yok
>>> pirnt(k4| k5) # set unıon bırleştırme ıslemi
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    pirnt(k4| k5) # set unıon bırleştırme ıslemi
NameError: name 'pirnt' is not defined
>>> print(k4 | k5)  # set unıon bırleştırme ıslemi
{'y', 'd', 'u', 'h', 'a', 'z', 'c', 's', 'n', 'v', 'ı', 'b', 'e', 'f', 'r', 'm', 'o', 'l', 'g', 'k', 't'}
>>> 
>>> 
>>> print(k4-k5)
{'k', 'o', 'z', 'c'}
>>> 
>>> # k4 de olan k5 te olmayanları bastık
>>> 
>>> print (k4 & k5) # kesişim
{'u', 'l', 'g', 'ı', 'e', 'r', 'm'}
>>> 
