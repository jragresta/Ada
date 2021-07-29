#Account Generator - v2
student_info = [
             {
                 "name": "ROSIE MARTINEZ",
             },
             {
                 "name": "JOE LIU",
             },
             {
                 "name": "SALLY SUE",               
             },
             {
                 "name": "BOB JOHNSON",               
             },
             {
                 "name": "DELIA AGHO",            
             },
]

import random

for kid in student_info:
  idNumber = random.randint(111111, 999999)
  kid["id"] = idNumber
  number = (str(idNumber))[-3:]
  [first,last] = kid["name"].split(" ")
  email = (f"{first[0]}{last}{number}@example.org")
  kid["email"] = email

for i in range (len(student_info)):
  print(f"name: {names[i]}")
  print(f"id: {ids[i]}")
  print(f"email: {emails[i]}\n")