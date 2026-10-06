import copy
numbers = [1,2,3,4,5]
print(numbers)

numbers = [1,2,3,4,5,3]
print(numbers,type(numbers))
print(numbers[0])
print(numbers[3:])
print(numbers[:0])
print(len(numbers))


str=list([1,30,14])
print(str,type(str))


num = [1,2,3,4,5]
num.append(6)
num.insert(0,5)
num.extend([10,20,30])
print(num)

#removing the number
num.pop()
num.pop(5)
num.remove(20)
num.clear()
print(num)

numbers = [1,2,3,4,5,2]
numbers[5]= 8
numbers[2:5]=[100,200,300]
print(numbers)

a=[10,20,30]
b = a.copy
print(b)

x=[2,4,5,1,8]
x.sort()
x.reverse()
print(x)

x =[4,5,6,7]
x.sort(reverse=True)
print(x)