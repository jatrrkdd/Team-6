from tkinter import *
from tkinter import ttk

from threading import Thread

import hashlib
import re

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
		route, account, permission_level, title, dept,
		archived, password and email: all strings

		Methods:
	"""
	#constructor
	def __init__( self, id, first_name=None,last_name=None,address=None,city=None,state=None,zip=None,classification=None,
	salary=None,commissioned=None,hourly=None,office_phone=None,DOB=None,SSN=None,
	start_date=None,route=None,account=None,permission_level=None,title=None,dept=None,
	archived=None,password=None,email=None):
		"""all parameters should be strings"""
		#set all fields to paramters
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.address = address
		self.city = city
		self.state = state
		self.zip = zip
		self.classification = classification
		self.salary = salary
		self.commissioned = commissioned
		self.hourly = hourly
		self.office_phone = office_phone
		self.DOB = DOB
		self.SSN = SSN
		self.start_date = start_date
		self.route = route
		self.account = account
		self.permission_level = permission_level
		self.title = title
		self.dept = dept
		self.archived = archived
		self.password = password #not hashed only hashed by edit employee
		self.email = email
	
	def employee_from_line( database_line):
		"""
			set_fields_from_line(database_line)
			takes in line from database and sets fields to
			those in database_line
		"""
		#takes in line from employee.csv as argument
		#split input line
		fields = database_line.strip().split(",")

		#if field has empty space set it to None. Empty fields are saved as " " in database
		for i in range(len(fields)):
			if fields[i] == " ":
				fields[i] = None

		#if split line doesn’t contain enough fields use old database format
		if len(fields) == 11: #old database contains 11 fields
			#pass all fields to constructor, fields come in same order a parameters in constuctor
			default_password = password_to_hash(fields[0],"12345")
			return Employee(fields[0], fields[1],fields[2],
			fields[3],fields[4],fields[5],
			fields[6],fields[7],fields[8],
			fields[9],fields[10],permission_level = 0,
			archived = "False", password = default_password)

		elif len(fields) == 23: #new database contains 22 fields
			#pass all fields to constructor, fields come in same order a parameters in constuctor
			return Employee( fields[0],fields[1],fields[2],
			 fields[3],fields[4],fields[5],
			 fields[6],fields[7],fields[8],
			 fields[9],fields[10],fields[11],
			 fields[12],fields[13],fields[14],
			 fields[15],fields[16],fields[17],
			 fields[18],fields[19],fields[20],
			 fields[21],fields[22])
		else:
			#unrecognized format
			raise ValueError("Unrecognized database format")

	def __str__(self):
		#put all fields of employee into csv line
		return (f'{self.id           or " "},{self.first_name     or " "},{self.last_name        or " "},'
			    f'{self.address      or " "},{self.city           or " "},{self.state            or " "},'
				f'{self.zip          or " "},{self.classification or " "},{self.salary           or " "},'
				f'{self.commissioned or " "},{self.hourly         or " "},{self.office_phone     or " "},'
				f'{self.DOB          or " "},{self.SSN            or " "},{self.start_date       or " "},'
				f'{self.route        or " "},{self.account        or " "},{self.permission_level or " "},'
				f'{self.title        or " "},{self.dept           or " "},{self.archived         or " "},'
		        f'{self.password     or " "},{self.email          or " "}')#the value or " " makes all None fields export as " "
	
	def update( self, updated_employee):
		"""
			sets self's fields to those in updated employee if not none
			doesn't update id
		"""
		#check if given employee is valid
		if not updated_employee.is_valid_employee():
			return False #not valid do nothing

		#update all fields if updated_employee does not have None for value
		self.first_name = updated_employee.first_name or self.first_name
		self.last_name = updated_employee.last_name or self.last_name
		self.address = updated_employee.address or self.address
		self.city = updated_employee.city or self.city
		self.state = updated_employee.state or self.state
		self.zip = updated_employee.zip or self.zip
		self.classification = updated_employee.classification or self.classification
		self.salary = updated_employee.salary or self.salary
		self.commissioned = updated_employee.commissioned or self.commissioned
		self.hourly = updated_employee.hourly or self.hourly
		self.office_phone = updated_employee.office_phone or self.office_phone
		self.DOB = updated_employee.DOB or self.DOB
		self.SSN = updated_employee.SSN or self.SSN
		self.start_date = updated_employee.start_date or self.start_date
		self.route = updated_employee.route or self.route
		self.account = updated_employee.account or self.account
		self.permission_level = updated_employee.permission_level or self.permission_level
		self.title = updated_employee.title or self.title
		self.dept = updated_employee.dept or self.dept
		self.archived = updated_employee.archived or self.archived
		self.password = updated_employee.password or self.password
		self.email = updated_employee.email or self.email

		return True

	def is_valid_employee(self):
		"""is_valid_emloyee()
		returns true if all fields are valid and false if not. None values are ignored"""
		is_valid = True

		return True #assumed valid for now valid tests are not done

		if self.id and not re.search("",self.id):
			return False #id is bad
		if self.first_name and not isinstance(self.first_name,str):
			return False #first_name is bad
		if self.last_name and not isinstance(self.last_name,str):
			return False #last_name is bad
		if self.address and not isinstance(self.address,str):
			return False #id is bad
		if self.city and not isinstance(self.city,str):
			return False #id is bad
		if self.state and not isinstance(self.state,str):
			return False #id is bad
		if self.zip and not re.search("^\d{5}$",self.zip):
			return False #zip is bad

		if self.classification:
			if not is_numeric(self.classification):
				return False
			if int(self.classification) > 2:
				return False #class is bad
		if not re.search("",self.salary):
			return False #id is bad
		if not re.search("",self.commissioned):
			return False #id is bad
		if not re.search("",self.hourly):
			return False #id is bad
		if not re.search("",self.office_phone):
			return False #id is bad
		if not re.search("",self.DOB):
			return False #id is bad
		if not re.search("",self.SSN):
			return False #id is bad
		if not re.search("",self.start_date):
			return False #id is bad
		if not re.search("",self.route):
			return False #id is bad
		if not re.search("",self.account):
			return False #id is bad
		if not re.search("",self.permission_level):
			return False #id is bad
		if not re.search("",self.title):
			return False #id is bad
		if not re.search("",self.dept):
			return False #id is bad
		if not re.search("",self.archived):
			return False #id is bad
		if not re.search("",self.email):
			return False #id is bad


		return is_valid


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
		self._load_employee_database.join(timeout=5)

		if self._load_employee_database.is_alive():
			#if loading isn't done after timeout return None
			return None

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

	def find_employees( self, name=None, id=None, title=None):
		"""find_employees( name, id, title)
		returns employee objects with matching name(first or last), id, and title. All are optional, just set unused to None.
		Not case sensitive"""
		#create list of found employees
		found_employees = []

		#remove casing
		if name:
			name = name.lower()
			
		if title:
			title = title.lower()

		#loop through employees
		for employee in self.employees:
			if name:
				#check if name matches or is substring
				in_first_name = name in employee.first_name.lower()
				in_last_name = name in employee.last_name.lower()
				if not (in_first_name or in_last_name):#if name isn't in first or last continue
					#if not continue
					continue

			#check if id matches or is substring
			if id:
				if not id in employee.id:
					#if not continue
					continue

			#check if title matches or is substring
			if title:
				#if employee title is none or title not in employee title
				if not employee.title  or not title in employee.title.lower(): 
					#if not continue
					continue

			#after all checks employee matches filters add to found list
			found_employees.append(employee)

		#return found employees
		return found_employees

	def add_employee( self, new_employee):
		"""add_employee( employee)
		adds new employee object to list does nothing if employee already exists(has same id)"""
		#loop through employees
		for employee in self.employees:
			#check if employee id matches existing employee
			if employee.id == new_employee.id:
				return #two employees should not have the same id
	
		#if does not match any existing add to employees list
		self.employees.append(new_employee)
		
		#save changes
		self.save_database()

	def remove_employee( self, id):
		"""remove_employee( id):
		removes employee with corresponding id"""

		#loop through employees
		for i in range(len(self.employees)):
			#if id matches employee id then remove from employee list
			if self.employees[i].id == id:
				self.employees.pop(i)
				#loop through time cards and receipts and remove any related records

				self.save_database()#save changes

				return #there should only be one employee matching id

	def edit_employee( self, updated_employee):
		"""edit employee( employee):
		updates the old employee data with data in updated_employee
		if field in updated_employee is None it is ignored. Use " " to clear field.
		updated_employee must have id set to work
		if password is given then password is hashed when set
		returns True if all fields are valid False if one is invalid"""
		#loop through employees database
		for employee in self.employees:
			#if employee matches looped employee
			if employee.id == updated_employee.id:
				#update attribute of looped employee to reflect changes
			
				if employee.update(updated_employee):#update returns false if updated_employee is invalid
					#save changes
					self.save_database()
					return True
				else:
					return False


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
				newEmployee = Employee.employee_from_line(line)
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
