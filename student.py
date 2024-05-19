#!/usr/bin/env python3
from datetime import date

class Student:
	threshold = 75 # class attribute

	def __init__(self, name, age, course, cohort):
		self.name = name
		self.age = age
		self.course = course
		self.cohort = cohort

	def __str__(self):
		return (
		f"Name: {self.name}\nAge: {self.age}"
		f"\nCourse: {self.course}\nCohort: {self.cohort}"
	)
		
	def defer(self, to_cohort, option="start as fresh"):
		if self.cohort == to_cohort:
			print (f"You're actually in the cohort {to_cohort}")
			return

		print(f"Bye then, Good luck {self.name}.")
		print(f"You've deffered to cohort {to_cohort}.")
		print(f"And you have chosen to {option}")

		self.cohort = to_cohort

	@classmethod
	def update_threshold(cls, new_threshold):
		cls.threshold = new_threshold

	@staticmethod
	def is_captains_log_day(day)
		if date.isoweekday() >= 5 and date.isoweekday() <= 7:
			return True

		return False



class RemoteStudent(Student):
	pass

student_1 = Student("Amr Sal", 28, "Software Engneer", 22)
student_2 = Student("Mohammed Sal", 28, "Software Engineer", 19)

print(student_1, end="\n\n")
print(student_2, end="\n\n")

result = student_1is_captains_log_day(date(2024, 2, 5))

if result is True:
	print("Today is a Captain's log day. Have you logged it yet?")else:
	print("Today is not a Captain's log day. Enjoy your day")
