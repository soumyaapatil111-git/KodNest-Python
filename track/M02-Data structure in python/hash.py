class student:
    def __init__(self, student_name, student_id):
        self.student_name=student_name
        self.student_id=student_id

    def __hash__(self):
        return hash(self.student_name, student_id)
student=student("john","101")
print(hash("student_name"))
print(hash("student_id"))

#hashing with dict
student={"name":"soumya", "age":22, "course":"python"}
print(student["name"])
print(student["age"])

#hashing with set
numbers={10, 20, 30, 20, 10}
print(numbers)