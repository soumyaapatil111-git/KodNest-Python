student = {
    "name": "Amit",
    "name": "Rahul",
    "age": 21,
    "course": "Computer science",
    "Tech": ["Computer science","Python","SQL"]
}
student["age"]=25
student.update({'cgpa' : 8.5})
print(student["age"])
print(student,type(student), len(student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("cgpa"))

print(student.pop("course"))
student.popitem()
student.clear()
del student


student={
    "name": "Rahul",
    "age": 23,
    "Tech": ["Python","SQL"]
}

student.setdefault("age", 22)
print(student)

keys = ["name","age","course"]
y=0

student=dict.fromkeys(keys, y)
print(student)

my_dict = student.copy()
print(my_dict)
my_dict.update({'name': "Amit"})
print(my_dict)

#using for loop in dict

student={
    "name": "Rahul",
    "language": "java",
    "marks": 85
}
for x in student:
    print(f"(x) =>{student}")

for x in student.items():
    print(x)

for x in student.keys():
    print(x)

for x in student.values():
    print(x)

#nested dic

students={
    "stu1": {
        "name": "Rahul",
        "age": 23,
        "Tech": ["Python","SQL"]
    },
    "stu2": {
        "name": "Amit",
        "age": 23,
        "Tech": ["java","SQL"]
    }
}

print(students)
print(students["stu2"]["name"])


    


products=[
    ["P101", "Keyword", 1200],
    ["P102", "MOUSE", 600],
     ["P103", "MOUNITOR", 8500]
]

required_code="P103"

for product in products:
    if product[0]==required_code:
        print(product)
        break


products={
    "P101": ["Keyword", 1200],
    "P102": ["MOUSE", 600],
    "P103": ["MOUNITOR", 8500]
}
print(products["P103"])

# employee
employees=[
    {"employee_id": "E101", "name": "Asha", "department": "Development"},
    {"employee_id": "E102", "name": "Ravi", "department": "testing"},
    {"employee_id": "E103", "name": "Simhadri", "department": "web developer"}
]
print(employees)
employee_by_id=()
for employee in employees:
    employee_id= employee["employee_id"]
    employee_by_id[employee_id]=employee

print(employee_by_id)

#GROUPING

students=[
    {"name":"asha", "course":"python"},
    {"name":"ravi", "course":"java"},
    {"name":"meera", "course":"python"},
]
