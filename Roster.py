#!/usr/bin/python3

class Roster:

	def __init__(self):
		self.students = []
	
	def add(self, student):
		"""
		adds a student to the roster
		"""
		self.students.append(student)

	def summarize(self):
		"""
		prints each student's profile information
		"""
		for student in self.students:
			print('-' * 40)
			print('Contact information for {0}. {1} is: '.
					format(student.first_name[0], student.last_name))
			print('-' * 40)
			student.print_info()
