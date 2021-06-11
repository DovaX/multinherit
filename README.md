# Multinherit
Package solving problems with super() builtin for classes with multiple inheritance.


## Motivation - Why Multinherit?
Multinherit solves the problems with super() builtin for classes with multiple inheritance.
It happens quite often that you cannot use neither super() builtin to call just one parent class __init__ nor both with different parameters. So in order to get something like the following code one needs to refactor the classes in the middle (B and C) in order for this to work.

```
class A(object):
    def __init__(self, a):
        self.a = a
        print(self.a)


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
        print(self.b)


class C(A):
    def __init__(self, a, c):
        super().__init__(a)
        self.c = c
        print(self.c)


class D(B, C):
    def __init__(self, a, b, c, d):
        #super().__init__(a, b, c)# -> Does not work -> Problem!
        self.d = d
        print(self.d)
        
print()
print("d1") 
d1=D(1,2,3,4)

>>> d1
>>> 4
```
A possible fix would be to write it like this
```
class A(object):
    def __init__(self, a):
        self.a = a
        print(self.a)


class B(A):
    def __init__(self, a, b):
        A.__init__(self,a)
        self.b = b
        print(self.b)


class C(A):
    def __init__(self, a, c):
        A.__init__(self,a)
        self.c = c
        print(self.c)


class D(B, C):
    def __init__(self, a, b, c, d):
        B.__init__(self,a,b)
        C.__init__(self,a,c)
        self.d = d
        print(self.d)
   

print()
print("d2")             
d2=D(1,2,3,4)

>>> d2
>>> 1
>>> 2
>>> 1
>>> 3
>>> 4
```
But it obviously initializes A.__init__ twice. In order to fix this, use multi_super function from multinherit package.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install multinherit.

```
pip install multinherit
```

## Usage

```
from multinherit.multinherit import multi_super

class A(object):
    def __init__(self, a):
        self.a = a
        print(self.a)


class B(A):
    def __init__(self, a, b):
        multi_super(A,self,a=a)
        self.b = b
        print(self.b)


class C(A):
    def __init__(self, a, c):
        multi_super(A,self,a=a)
        self.c = c
        print(self.c)


class D(B, C):
    def __init__(self, a, b, c, d):
        multi_super(B,self,a=a,b=b)
        multi_super(C,self,a=a,c=c)
        self.d = d
        print(self.d)
   

print()
print("d3")            
d3=D(1,2,3,4)
print(d3._classes_initialized)

>>> d3
>>> 1
>>> 2
>>> 3
>>> 4
>>> [<class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>]
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
