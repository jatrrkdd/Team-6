from tkinter import *
from tkinter import ttk

from threading import Thread

import hashlib

#example database employees with password "12345" and all fields
#12-3456789,Bob,Tester,894 Glendale Plaza,Worcester,Massachusetts,1610,2,62862.15,46,16.85,123-456-7890,3/24/2023,123-45-6789,3/24/2023,30417353-K,465794-3611,0,assitant to the manager,stapler,False,4e4577f023d1c8ab0deb91ecc1cc4f51a0cd232e0b91e60c8811e6c82da60956,bob@bob.com
#12-3456790,Bob,Tester The Second,894 Glendale Plaza,Worcester,Massachusetts,1610,2,62862.15,46,16.85,123-456-7890,4/25/2023,123-45-6790,4/25/2023,30417354-K,465794-3611,1,assitant to the assistant to the manager,stapler,False,adabe0c70c26f8850c41a6ddb969db8f3de122c203af1beed2953b18e8fb2776,bob2@bob.com
#12-3456791,Bob,Tester The Third,894 Glendale Plaza,Worcester,Massachusetts,1610,2,62862.15,46,16.85,123-456-7891,4/26/2023,123-45-6791,4/26/2023,30417355-K,465794-3611,1,assitant to the assitant to the assistant to the manager,stapler,False,100b16b5ee41ec5bb14087101261e0193b2db7ebbd2fc6739a41599d8654a91e,bob3@bob.com		


def password_to_hash( id, password):
	"""Takes in id and password as strings and returns string of hashed password
		uses id as salt
	"""
	id_in_bytes = bytes(id, "utf-8")
	password_in_bytes= bytes(password, 'utf-8')
	return hashlib.pbkdf2_hmac('sha256', password_in_bytes, id_in_bytes, 500).hex()

#Employee class
class Employee:
	"""
		Used to store all of an employee’s data
		Attributes:
		id, first_name, last_name, address, city, state, zip, classification,
		salary, commissioned, hourly, office_phone, DOB, SSN, start_date,
		bank_info, permission_level, title, dept,
		archived, password and email: all strings

		Methods:
	"""
	#constructor
	def __init__( self, database_line):
		#takes in line from employee.csv as argument
		#split input line
		fields = database_line.strip().split(",")
		#if split line doesn’t contain enough fields use old database format
		if len(fields) == 11: #old database contains 11 fields
			#set each attribute to corresponding index in split input line
			self.id = fields[0]
			self.first_name = fields[1]
			self.last_name = fields[2]
			self.address = fields[3]
			self.city = fields[4]
			self.state = fields[5]
			self.zip = fields[6]
			self.classification = fields[7]
			self.salary = fields[8]
			self.commissioned = fields[9]
			self.hourly = fields[10]
			self.office_phone = " "
			self.DOB = " "
			self.SSN = " "
			self.start_date = " "
			self.route = " "
			self.account = " "
			self.permission_level = 0
			self.title = " "
			self.dept = " "
			self.archived = "False"
			self.password = password_to_hash(self.id,"12345")
			self.email = " "
		elif len(fields) == 23: #new database contains 22 fields
			#set each attribute to corresponding index in split input line
			self.id = fields[0]
			self.first_name = fields[1]
			self.last_name = fields[2]
			self.address = fields[3]
			self.city = fields[4]
			self.state = fields[5]
			self.zip = fields[6]
			self.classification = fields[7]
			self.salary = fields[8]
			self.commissioned = fields[9]
			self.hourly = fields[10]
			self.office_phone = fields[11]
			self.DOB = fields[12]
			self.SSN = fields[13]
			self.start_date = fields[14]
			self.route = fields[15]
			self.account = fields[16]
			self.permission_level = fields[17]
			self.title = fields[18]
			self.dept = fields[19]
			self.archived = fields[20]
			self.password = fields[21]
			self.email = fields[22]
		else:
			#unrecognized format
			raise ValueError("Unrecognized database format")
	def __str__(self):
		#put all fields of employee into csv line
		return (f"{self.id},{self.first_name},{self.last_name},"
			    f"{self.address},{self.city},{self.state},{self.zip},{self.classification},"
		        f"{self.salary},{self.commissioned},{self.hourly},{self.office_phone},{self.DOB},{self.SSN},"
		        f"{self.start_date},{self.route},{self.account},{self.permission_level},{self.title},{self.dept},{self.archived},"
		        f"{self.password},{self.email}")




#Database class
class Database():
	"""
		Access to the database files
		Attributes:
		app: reference to Application instance
		database_location: file path to database
		employees: list of employee objects
		timecards: list of timecards
		Receipts: list of receipts
		_employee_loader_thread: thread to load employee data
		_timecard_loader_thread: thread to load timecard data
		_reciept_loader_thread: thread to load receipt data
		Methods:
		check_login( id, password): returns employee object if login successful
		find_employees( name, id, title): returns employee objects with matching name, id, and title. All are optional, just set unused to None.
		add_employee( employee): adds new employee object to list
		remove_employee( id): removes employee with corresponding id
		edit employee( employee): updates the old employee data with data in employee
		generate_pay_report( file_path): creates pay report with data in database at file_path
		generate_database_report( file_path): creates database report with data in database at file_path
		_load_employee_database( file_path): loads data from employee.csv at file_path
		_load_timecards_database( file_path): loads data from timecards.csv at file_path
		_load_receipts_database( file_path): loads data from receipts.csv at file_path
		compute_employee_payment( employee): returns string of payment info for report e.g.“Mailing 5599.44 to Issie Schalard at 11 Texas Court Columbia Missouri 65218”
		employee_report( employee): Returns string for database report
	"""

	#Database constructor
	def __init__( self, app, database_location):
		"""Database class Constructor
			Takes in Application class and database file_location
		"""
		#set app to given parameter
		self.app = app
		#set database_location to given parameter
		self._database_location = database_location
		self.employees = []
		self.timecards = []
		self.receipts = []

		#set if error occurs when loading database. The file doesn't exist
		self.loading_database_error = False 

		#create thread to run _load_emplyee_database
		employee_csv_path = database_location+"new_employees.csv" #using new_employees.csv so old doesn't get overwritten
		self._load_employee_database = Thread(target=self._load_employee_database, args=[employee_csv_path],daemon=True)
		#create thread to run _load_timecards_database
		#create thread to run _load_reciepts_database
		
		self._load_employee_database.start()

	#Destructor
	def save_database( self):
		"""Save current database to files
			Call this after making changes to database
		"""
		#open employee.csv file
		employee_csv_path = self._database_location+"new_employees.csv" #using new_employees.csv so old doesn't get overwritten
		employee_output_file = open( employee_csv_path,'w+')
		csv_header = ("id, first_name, last_name, address, city, state, zip, classification,"
					"salary, commissioned, hourly, office_phone, DOB, SSN, start_date,"
					"rounte, account, permission_level, title, dept,"
					"archived, password, email\n")

		employee_output_file.write(csv_header)
		#loop through employees list
		for employee in self.employees:
			#Write line containing employee info
			employee_output_file.write(str(employee)+"\n")
		#close employee.csv
		employee_output_file.close()

		#open timecards.csv
		#loop through timecards
		#Write line containing timecard info
		#close timecards.csv
		#open receipts.csv
		#loop through receipts
		#Write line containing receipt info
		#close receipts.csv

	"""check_login( id, password)
	returns employee object if login successful"""
	def check_login( self, id, password):
		#check if _load_employee_database thread is done
		timeout = 5 #timeout 5 seconds database shouldn't take that long to load
		if self._load_employee_database.is_alive():
			#if loading isn't done wait
			self._load_employee_database.join()
		#loop through employees list
		for employee in self.employees:
			#if id matches employee
			if employee.id == id:
				#if password matches employee password
				password_hash = password_to_hash( id, password)
				if employee.password != " " and employee.password == password_hash:
					#Return current looped employee
					return employee
				else:
					print("wrong password")
				return None #id's are unique
					
		#return None login does not match
		return None

	"""find_employees( name, id, title)
	returns employee objects with matching name, id, and title. All are optional, just set unused to None."""
	#create list of found employees
	#loop through employees
		#check if name matches or is substring
			#if not continue
		#check if id matches or is substring
			#if not continue
		#check if title matches or is substring
			#if not continue
		#after all checks employee matches filters add to list
	#return found employees

	"""add_employee( employee)
	adds new employee object to list"""
	#loop through employees 
		#check if employee id matches existing employee
	#if does not match any existing add to employees list

	"""remove_employee( id):
	removes employee with corresponding id"""
	#loop through employees
		#if id matches employee id then remove from employee list
			#loop through time cards and receipts and remove any related records

	"""edit employee( employee):
	updates the old employee data with data in employee"""
	#loop through employees database
		#if employee matches looped employee
			#update attribute of looped employee to reflect changes


	"""generate_pay_report( file_path, hourly, salaried, commissioned): creates pay report with data in database at file_path"""
	#open file for export
	#if hourly	
	#loop through employees
		#if employee is hourly
		#call compute_employee_payment() method
			#add string to output file
	#if salaried	
	#loop through employees
		#if employee is salaried
		#call compute_employee_payment() method
			#add string to output file
	#if commissioned	
	#loop through employees
		#if employee is commissioned
		#call compute_employee_payment() method
			#add string to output file
	#close file

	"""generate_database_report( file_path, export_all, current,archived): creates database report with data in database at file_path. Current is a list of employees given by search page"""
	#open file for export
	#if export_all	
	#loop through employees
	#call employee’s employee_report() method
		#add string to output file
	#return
	#if current != None	
	#loop through current
	#call employee_report() method
		#add string to output file
		#return
	#if archived	
	#loop through employees
		#call employee_report() method
			#add string to output file
	#close file

	def _load_employee_database( self, file_path):
		"""_load_employee_database( file_path):
		loads data from employee.csv at file_path
		file_path includes file name and exstention
		"""
		#open employee.csv at file_path
		employee_file = open( file_path, 'r')
		#if the file doesn't exist….. Uh oh

		#loop through employee.csv line by line
		line = employee_file.readline() #database has header take it off top
		while line:
			#get line for employee
			line = employee_file.readline()
			if line != "":
				#create new employee passing line to employee constructor
				newEmployee = Employee(line)
				#add employee to employees list
				self.employees.append(newEmployee)
		employee_file.close()

	"""_load_timecards_database( file_path):
	loads data from timecards.csv at file_path"""
	#open timecards file
	#check if file exists
	#loop through file line by line
		#split line
		#if numbers of elements > 3 then its old database
			#add list of 3 to receipts list with id, time timecard was entered, and hours for each column except id
		#if number of elements = 3 assume its new database
			#add list of 3 to receipts list with id, time, and hours


	"""_load_reciepts_database( file_path):
	loads data from receipts.csv at file_path"""
	#open receipts file
	#check if file exists
	#loop through file line by line
		#split line
		#if numbers of elements > 3 then its old database
			#add list of 3 to receipts list with id, time, and amount for each column except id
		#if number of elements = 3 assume its new database
			#add list of 3 to receipts list with id, time, and amount

	"""compute_employee_payment( employee):
	returns string of payment info for payroll report for employee e.g.“Mailing 5599.44 to Issie Schalard at 11 Texas Court Columbia Missouri 65218”
	"""
	#calculate employee’s pay
	#create variable total pay
	#if employee hourly
		#create variable to hold total hours
		#loop through time cards
			#if id matches employee
				#add hours to total hours
		#compute total_pay
	#elif employee salaried
		#compute total_pay based on employee object
	#elif employee commissioned
		#compute total_pay based on employee salary
		#loop through receipts
			#if id matches employee id
				#add commission to total pay

	#create payment_string
	#if employee direct deposit(paymethod 1)
	#create string for direct deposit with total pay
	#elif employee mail (paymethod 2)
		#create string for mail with total pay
	#return payment_string

	"""employee_report( employee):
	Returns string of employee for database report"""
	#create report string with employee info
	#return string
