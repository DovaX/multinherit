from multinherit import multi_super

"""Problem - cannot do neither super() builtin to call just one parent class __init__ nor both with different parameters"""

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


"""Possible fix - but initializes A.__init__ twice - might be wrong"""

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


"""Fix using multinherit"""

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