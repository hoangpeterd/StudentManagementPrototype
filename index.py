#!/usr/bin/python3

from helpers import *

from Roster import Roster

from Student import Student

# class roster
roster = Roster()

while True:

	# get information and assign via unpacking, and then intantiate a new student
	first, last, middle, address, email, phone = get_student_information()
	student = Student(first, last, middle, address, email, phone)

	student.print_info()
	# prompt for confirmation
	if confirm('Is this information correct? (Y/N) '):
		roster.add(student)

		if confirm('Would you like to add a student to the roster? (Y/N) '):
			continue
		else:
			roster.summarize()
			break