import json

try:
    with open('testingArea\\students_authenticator\\students.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("file was not found")
    exit()

students = data.get('students', [])

student_input = input("Enter student name: ")

for student in students:
    if student["name"].lower() == student_input.lower():
        found_student = student
        break

if found_student is None:
    print("Student not found")

reg_key_input = input("Enter the registration key: ")

if found_student["registration_key"] == reg_key_input:
    print("")



