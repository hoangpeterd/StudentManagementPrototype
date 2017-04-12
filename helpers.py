#!/usr/bin/python3

# helpers module for student information script

def get_student_information():
	# prompt user to input student's identification information
	first = input('Please enter the student\'s first name: ')
	last = input('Please enter the student\'s last name: ')
	middle = input('Please enter the student\'s middle initial: ')

	# prompt user for student's contact information
	address = input('Please enter the student\'s address: ')
	email = input('Please enter the student\'s email: ')
	phone = input('Please enter the student\'s phone number: ')

	return [first, last, middle, address, email, phone]

def create_student(**student):
	"""
	create_student creates a student dictionary with the data contained in the information array
	"""

	_student = dict.fromkeys(['first_name', 'last_name', 'middle_initial', 'address', 'email', 'phone_number'])

	# identification information
	_student['first_name'] = student.get('first_name', 'N/A')
	_student['last_name'] = student.get('last_name', 'N/A')
	_student['middle_initial'] = student.get('mmiddle_initial', 'N/A')

	#contact information
	_student['address'] = student.get('address', 'N/A')
	_student['email'] = student.get('email', 'N/A')
	_student['phone_number'] = student.get('phone_number', 'N/A')

	return _student

def print_separator(repetitions = 18):
	print('-' * repetitions)

def print_student(student):
	print('You\'ve entered: ')

	print_separator()

	for key, value in student.items():
		print('The student\'s {0} is {1}.'.format(key, value))

	print_separator()

def confirm(message):
	confirmation = (input(message).lower() == 'y')
	return confirmation

def print_summary(students):
	print('You\'ve entered the following profiles: ')

	print_separator()

	for student in students:
		print_student(student)

	print_separator()