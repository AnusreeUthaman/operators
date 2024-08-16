
#arithematical operators
a=8
b=5
c=a-b
print(c)

a=8
b=5
c=a*b
print(c)

a=8
b=5
c=a/b
print(c)

a=8
b=5
c=a%b
print(c)

a=3
b=2
c=a**b
print(c)

a=3
b=2
c=a//b
print(c)


#comaprison operators
a=2
b=3
c=b==a
print(c)
a=2
b=2
c=b==a
print(c)
a=2
b=3
c=b!=a
print(c)
a=2
b=3
c=b>a
print(c)
a=2
b=3
c=b<a
print(c)
a=2
b=3
c=b<=c
print(c)
a=2
b=3
c=b>=c
print(c)


#logical operators
a=True
b=False
print(a and b)
a=True
b=True
print(a and b)
a=True
b=False
print(a or b)
a=True
b=True
print(a or b)
a=False
b=False
print(a or b)
a=3
b=0
print(a or b)
print(a and b)



#inplace operators
a=10
a+=15
print(a)
a=10
a-=15
print(a)
a=10
a/=15
print(a)
a=10
a*=15
print(a)
a=10
a//=15
print(a)
a=10
a**=15
print(a)
a=10
a%=15
print(a)



#identity operators- is,is not
a=5
b=5
print(id(a))
print(id(b))
a=5
b=6
print(id(a))
print(id(b))
a=10
b=5
c=10
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)
print(a is not b)
print(a is not c)


#membership operators-in,not in
x="This is a text"
print("tex" in x)
print("is  " in x)
print("text" not in x)
print("at" not in x)


