#!/usr/bin/env python3
from student import Student

student_1 = Student("Amr Sal", 28, "Software Engneer", 22)
student_2 = Student("Mohammed Sal", 28, "Software Engineer", 19)

print(student_1, end="\n\n")
print(student_2, end="\n\n")

result = student_1is_captains_log_day(date(2024, 2, 5))

if result is True:
        print("Today is a Captain's log day. Have you logged it yet?")else:
        print("Today is not a Captain's log day. Enjoy your day")
