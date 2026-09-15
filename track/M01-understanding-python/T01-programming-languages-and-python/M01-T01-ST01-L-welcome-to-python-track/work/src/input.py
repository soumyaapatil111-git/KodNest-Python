import numbers
name = input("enter the name :")
print(f"my name is{name} !")

age = input("enter the age :")
print(f"the age is{age}!")

a=int(input("a :"))
b=int(input("b :"))
c=a+b
print(c)

print("------identity operator")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x ==y)
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

print("-----ternary operator----")
num = 10
res = "Even" if num % 2 == 0 else "odd"
print(res)


a = 10
b = 20
c = 30
greatest = a if a > b and a > c else b if b > c else c
print(greatest)

num = -1
res = "postive" if num > 0 else "negative"
print(res)