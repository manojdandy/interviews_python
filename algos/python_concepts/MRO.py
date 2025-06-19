class A:
    def greet(self): print("A")

class B(A):
    #def greet(self): print("B")
    pass

class C(A):
   # def greet(self): print("C")
   pass

class D(B, C):  # Multiple inheritance
    pass

d = D()
d.greet()

print(D.mro())
print("********")
b = A()
b.greet()