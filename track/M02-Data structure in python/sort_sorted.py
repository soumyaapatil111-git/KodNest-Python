#sort and sorted
# we can use in set ,dic, tuple but not list, and also it create newlist

marks=[60, 30,45,20]
new_marks=sorted(marks)
print(new_marks)
print(marks)

#reversing
marks=[60, 30,45,20]
new_marks=sorted(marks,reverse=True)
print(new_marks)
print(marks)

#sort only in list, changes the original list
age=[2, 30,18,22,100]
age.sort()
print(age) 

#reversing
age=[2, 30,18,22,100]
age.sort(reverse=True)
print(age) 

names=["apple", "banana", "mango"]
names.sort()
print(names)


names={"apple","banana","mango"}
print(sorted(names))

# #cannot be used
# names={"apple", "banana", "mango"}
# names.sort()
# print(names)

cities=["Bengaluru", "Pune", "bengaluru", "chennai"]
unique_cities={city.lower() for city in cities}
print(unique_cities)


#nested list inside list
student_marks=[
    [78,85,91],
    [72,66,89]
]
print(student_marks)


#using index and change value
student_marks=[
    [78,85,91],
    [72,66,89]
]
student_marks[0][1]=90
print(student_marks)

#list inside the dict
student={
    "name":"asha",
    "skills":["python","sql","java"]
}
print(student["skills"])

#replaceing
student["skills"][2] ="javascript"
print(student)

#append
student["skills"].append("git")
print(student)
