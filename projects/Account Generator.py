#Account Generator
student_names = []
student_idNumbers = []
student_emails = []
import random

def new_student(first, last):
  firstname = first
  lastname = last

  name = (f"{first} {last}")
  student_names.append(name)

  idNumber = random.randint(111111, 999999)
  number = str(idNumber)
  student_idNumbers.append(idNumber)

  email = (f"{firstname[0]}{lastname}{number[0:3]}@example.org")
  student_emails.append(email)

new_student("John", "Smith")
new_student("Jane", "Doe")
new_student("Jack", "Oliver")
new_student("Kelsey", "Yee")
new_student("Karen", "Smithy")

for i in range(len(student_names)):
  print(f"name: {student_names[i]}\nid: {student_idNumbers[i]}\nemail: {student_emails[i]}")
  print("")
