Python 3.5.0 |Anaconda 2.4.0 (64-bit)| (default, Oct 20 2015, 07:26:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> set([1,2,3,4])
{1, 2, 3, 4}
>>> 
>>> set([set([1,2]),set([3,4])])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> 
>>> set([frozenset([1,2]),frozenset([3,4])])
{frozenset({1, 2}), frozenset({3, 4})}
>>> 
>>> A=set([1,2])
>>> S=set([frozenset([1,2]),frozenset([3,4])])
>>> A<S
False
>>> A in S
True
>>> A=set([frozenset([1,2])])
>>> print(A)
{frozenset({1, 2})}
>>> A<S
True
>>> 