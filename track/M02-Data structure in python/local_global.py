c=30
def add():
    a=20
    b=30 #local variable
    print(a+b)
    print(c)
add()
print(c)

x=100 #gloabl variable
def display():
    y=200
    print("Local y:",y)
display()
print("global x:",x)

x=10 #gloabl variable
def display():
    print(x)
display()
x=20
print(x)

#function overloading
#it is not possible in python bcz in pvm it take last value to over come we have default variable and variable aruguments

#default argument
def add(a,b=0,c=0,d=0):
    return a+b+c+d
print(add(10,20))
print(add(20))
print(add(10,20,30,40,))

#var arg represent by *args
# the result will be tuple form
def add(*args):
    return args
print(add(10,20))
print(add(10,20,30,40))

def add(*args):
    total=0
    for n in args:
        total+=n
    return total
print(add(10,20))
print(add())

#recursion 
def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(5)

#factorial
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

#fibbonacci series
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))