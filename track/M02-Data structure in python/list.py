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

#tuple

t= (10, 20, 30, 40,50)
print("Q1:", t[1:4])

t= (10, 20, 30, 40,50)
print("Q2:", t[1:4])

t= (10, 20, 30, 40,50)
print("Q3:", t[1:4])

t= (10, 20, 30, 40,50)
print("Q4:", t[1:4])

t= (10, 20, 30, 40,50)
print("Q5:", t[1:4])

t= (10, 20, 30, 40,50)
print("Q6:", t[:3])

t= (10, 20, 30, 40,50)
print("Q7:", t[2:])

t= (10, 20, 30, 40,50)
print("Q8:", t[-3:])

t= (10, 20, 30, 40,50)
print("Q9:", t[1:])

t= (10, 20, 30, 40,50)
print("Q10:", t[:-1])

t= (10, 20, 30, 40,50)
print("Q11:", t[::2])

t= (10, 20, 30, 40,50)
print("Q12:", t[::3])

t= (10, 20, 30, 40,50)
print("Q13:", t[::-1])

t= (10, 20, 30, 40,50)
print("Q14:", t[4:1:-1])

t= (10, 20, 30, 40,50)
print("Q16:", t[-4:-1])

t= (10, 20, 30, 40,50)
print("Q17:", t[-1:-4:-1])

t= (10, 20, 30, 40,50)
print("Q18:", t[1:2])

t= (10, 20, 30, 40,50)
print("Q19:", t[-5:-1:2])

t= (10, 20, 30, 40,50)
print("Q20:", t[-1:-5:-2])

t= (10, 20, 30, 40,50)
print("Q21:", t[1:100])

t= (10, 20, 30, 40,50)
print("Q22:", t[1:4][::-1])


marks = [10, 20, 30]
stu_marks = marks
stu_marks[0] = 100
print(marks)
print(stu_marks)


first = [1, 2, 3]
second = first
print(first is second)
print(first == second)


first = [1,2,3]
second = [1,2,3]
print(first is second)
print(first == second)

num = [10, 20]
values = num
values.append(30)
print(num)
print(values)

num = [10, 20]
values = num
values = [100,200]
print(num)
print(values)




