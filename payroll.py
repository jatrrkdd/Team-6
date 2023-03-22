'''
Takes information given on employees.csv, timecards.csv and receipts.csv
to create a representation of the employees, then processes the payroll of
specified employees. The employees are able to change between three types
of payroll: Hourly, Salaried and Commissioned. Meant to work with p5.py

Author: Derek Thompson

Classes:
	Classification
	Hourly
	Salaried
	Commissioned
	Employee
	
Functions:
	load_employees()
	find_employee_by_id(employee_id)
	process_timecards()
	process_receipts()
	process_file(file_name, header)
	run_payroll()
	clear_entries(row, type)
'''

from abc import ABC, abstractmethod
import os, os.path, shutil

PAY_LOGFILE = "payroll.txt"
employees = []
timecards = []
receipts = []

def load_employees():
	'''
	Populates employees with data from employees.csv
	'''
	EMPLOYEE_FILE = "employees.csv"
	file_data = process_file(EMPLOYEE_FILE, True)
	global employees
	for entry in range(len(file_data)):
		if file_data[entry]:
			employee = Employee(file_data[entry][0], file_data[entry][1],
			file_data[entry][2], file_data[entry][3], file_data[entry][4],
			file_data[entry][5], file_data[entry][6], file_data[entry][7],
			file_data[entry][8], file_data[entry][9], file_data[entry][10])
			employees.append(employee)
			
def find_employee_by_id(emp_id):
	'''
	Searches employees for a matching emp_id then returns which row it was
	found
	
	Parameters:
		emp_id: string
			Employee's id number
	
	Returns:
		Row in employees that matches emp_id
	'''
	global employees
	for entry in range(len(employees)):
		current = employees[entry].get_emp_string()
		if current == emp_id:
			return employees[entry]
			
def process_timecards():
	'''
	Populates timecards with data from timecards.csv
	'''
	TIMECARD_FILE = "timecards.csv"
	file_data = process_file(TIMECARD_FILE)
	for row in range(len(file_data)):
		for column in range(len(file_data[row])):
			try:
				file_data[row][column] = float(file_data[row][column])
			except:
				pass
	global timecards
	timecards = file_data
	
def process_receipts():
	'''
	Populates receipts with data from receipts.csv
	'''
	RECEIPT_FILE = "receipts.csv"
	file_data = process_file(RECEIPT_FILE)
	for row in range(len(file_data)):
		for column in range(len(file_data[row])):
			try:
				file_data[row][column] = float(file_data[row][column])
			except:
				pass
	global receipts
	receipts = file_data

	
def process_file(file_name, header=False):
	'''
	Returns data from specified csv file
	
	Parameters:
		file_name: string
			Name of csv file
		header: bool
			True if file contains a header that needs to be ignored,
			False no header exists, False by default
			
	Returns:
		Data in the form of a 2d list
	'''
	file_data = []
	with open(file_name, 'r') as f:
		line = f.readline()
		if not header:
			file_data.append(line.strip().split(","))
		while line:
			line = f.readline()
			if line != "":
				file_data.append(line.strip().split(","))
	return file_data
	
def run_payroll():
	if os.path.exists(PAY_LOGFILE):
		os.remove(PAY_LOGFILE)
	for emp in employees:
		emp.issue_payment()
		
def clear_entries(row, type):
	'''
	Clears a row of timecards or receipts
	
	Parameters:
		row: int
			Row to be cleared
		type: string
			Type of row to be cleared, valid inputs: timecard or receipt
	'''
	if type == "timecard":
		global timecards
		for column in len(timecards[row]):
			timecards[entry][column] = 0
	elif type == "receipt":
		global receipts
		for column in len(receipts[row]):
			receipts[entry][column] = 0
	else:
		raise ValueError("Invalid entry type.")
				
			

class Classification(ABC):
	'''
	An abstract class used as a template for the Classification type classes
	'''
	@abstractmethod
	def compute_pay(self):
		pass
		
class Hourly(Classification):
	'''
	A class used to manage the attributes of a Hourly employee
	
	Attributes:
		emp_string: string
			Employee's id number
		_hourly_rate: float
			Employee's hourly rate
			
	Methods:
		add_timecard(timecard=list)
			Adds timecard entry for specified employee, creates employee in 
			timecards if employee doesn't exist in timecards
		compute_pay()
			Returns employee's pay based on timecards and clears employee's
			timecard entries once paid
		_get_hourly_rate()
			Returns _hourly_rate
	'''
	def __init__(self, emp_string, hourly_rate=0):
		'''
		Creates the nessisary attributes for Hourly
		
		Parameters:
			emp_string: string
				Employee's id number
			_hourly_rate: float
				Employee's hourly rate, is 0 by default
		'''
		self.emp_string = emp_string
		self._hourly_rate = hourly_rate
		
	def add_timecard(self, timecard):
		'''
		Adds timecard entry for specified employee, creates employee in 
		timecards if employee doesn't exist in timecards

		Parameters:
			timecard: list
				list of hourly employee timecards taken from timecards.csv
		'''
		for entry in range(len(timecards)):
			if timecards[entry][0] == self.emp_string:
				timecards[entry].append(timecard)
				return
		timecards.append([self.emp_string, timecard])
		
	def compute_pay(self):
		'''
		Returns employee's pay based on timecards and clears employee's 
		timecrad entries once paid
		
		Returns:
			Employee's pay based on timecards and hourly_rate
		'''
		for entry in range(len(timecards)):
			if timecards[entry][0] == self.emp_string:
				total_time = sum(timecards[entry][1:])
				return round(total_time * float(self._get_hourly_rate()), 2)
				clear_entries(entry, "timecard")
					
		
	def _get_hourly_rate(self):
		return self._hourly_rate
		
		
class Salaried(Classification):
	'''
	A class used to keep the attributes of a Salaried employee
	
	Attributes:
		emp_string: string
			Employee's id number
		_salary_rate: float
			Employee's salary_rate
		_commission_rate: float
			Employee's commission_rate, None by default
			
	Methods:
		compute_pay()
			Returns employee's pay based on salary and commission_rates
		_get_salary_rate()
			Returns _salary_rate
	'''
	def __init__(self, emp_string, salary_rate=0, commission_rate=None):
		'''
		Creates the nessisary attributes for Salaried
		
		Parameters:
			emp_string: string
				Employee's id number
			_salary_rate: float
				Employee's salary_rate
			_commission_rate: float
				Employee's commission_rate, None by default
		'''
		self.emp_string = emp_string
		self._salary_rate = salary_rate
		self._commission_rate = commission_rate

		
	def	compute_pay(self):
		'''
		Returns employee's pay based on salary and commission_rates
		
		Returns:
			Employee's pay based on salary_rate, commission_rate and receipts
		'''
		if self._commission_rate:
			for entry in range(len(receipts)):
				if receipts[entry][0] == self.emp_string:
					total_receipts = sum(receipts[entry][1:])
					return round(float(self._get_salary_rate()) / 24 + 
					(total_receipts * (float(self._commission_rate ) / 100))
					, 2)
					clear_entries(entry, "receipt")
		else:
			return round(float(self._get_salary_rate()) / 24, 2)
		
	def _get_salary_rate(self):
		return self._salary_rate
		
		
class Commissioned(Salaried, Classification):
	'''
	A class used to keep the attributes of a Commissioned employee
	
	Attributes:
		emp_string: string
			Employee's id number
		_salary_rate: float
			Employee's salary_rate, 0 by default
		_commission_rate: float
			Employee's commission_rate, 0 by default
			
	Methods:
		add_receipt(receipt=list)
			Adds timecard entry for specified employee, creates employee in 
			timecards if employee doesn't exist in timecards
		_get_commission_rate()
			Returns _commission_rate
	'''
	def __init__(self, emp_string, salary_rate=0, commission_rate=0):
		'''
		Creates the nessisary attributes for Commissioned using Salaried
		
		Parameters:
			emp_string: string
				Employee's id number
			_salary_rate: float
				Employee's salary_rate, 0 by default
			_commission_rate: float
				Employee's commission_rate, 0 by default
		'''
		Salaried.__init__(self, emp_string, salary_rate, commission_rate)
		
	def add_receipt(self, receipt):
		'''
		Adds receipts entry for specified employee, creates employee in 
		receipts if employee doesn't exist in receipts

		Parameters:
			receipts: list
				list of commissioned employee receipts taken from receipts.csv
		'''
		for entry in range(len(receipts)):
			if receipts[entry][0] == self.emp_string:
				receipts[entry].append(receipt)
				return
		receipts.append([self.emp_string, receipt])
		
	def _get_commission_rate(self):
		return self._commission_rate
		
		
class Employee():
	'''
	An abstraction of an employee
	
	Attributes:
		emp_string: string
			Employee's id number
		_first_name: string
			Employee's first name
		_last_name: string
			Employee's last name
		_address: string
			Employee's address
		_city: string
			Employee's city
		_state: string
			Employee's state
		_zipcode: string
			Employee's zipcode
		classification: object
			An instance of the Classification classes, manages pay rates and 
			payroll
			
	Methods:
		make_salaried(salary_rate=float)
			Changes the Employee classification to an instance of Salaried
		make_commissioned(salary_rate=float, commission_rate=float)
			Changes the Employee classification to an instance of Commissioned
		make_hourly(hourly_rate=float):
			Changes the Employee classification to an instance of Hourly
		issue_payment():
			Computes employee's pay using classification then outputs to 
			payroll.txt
		get_emp_string():
			Returns emp_string
		_get_firstname():
			Returns _first_name
		_get_lastname():
			Returns _last_name
		_get_address():
			Returns _address
		_get_city():
			Returns _city
		_get_state():
			Returns _state
		_get_zipcode():
			Returns _zipcode
	'''
	def __init__(self, emp_string="", first_name="", last_name="", address="",
				city="", state="", zipcode="", classification=0, salary_rate=0,
				commission_rate=0, hourly_rate=0):
		'''
		Creates the nessisary attributes for Employee
		
		Parameters:
			emp_string: string, empty string by default
				Employee's id number
			_first_name: string, empty string by default
				Employee's first name
			_last_name: string, empty string by default
				Employee's last name
			_address: string, empty string by default
				Employee's address
			_city: string, empty string by default
				Employee's city
			_state: string, empty string by default
				Employee's state
			_zipcode: string, empty string by default
				Employee's zipcode
			classification: int
				Specifies the type of Classification, 1=Salaried, 
				2=Commissioned, 3=Hourly
			salary_rate: float
				Employee's salary rate
			commission_rate: float
				Employee's commission rate
			hourly_rate: float
				Employee's hourly rate
		'''
		self.emp_string = emp_string
		self._first_name = first_name
		self._last_name = last_name
		self._address = address
		self._city = city
		self._state = state
		self._zipcode = zipcode
		if classification == '1':
			self.make_salaried(salary_rate)
		elif classification == '2':
			self.make_commissioned(salary_rate, commission_rate)
		elif classification == '3':
			self.make_hourly(hourly_rate)
		else:
			raise ValueError("Invalid classification index")
			
	def make_salaried(self, salary_rate):
		'''
		Changes the Employee classification to an instance of Salaried
		
		Parameters:
			salary_rate: float
		'''
		self.classification = Salaried(self.emp_string, salary_rate)
	
	def make_commissioned(self, salary_rate, commission_rate):
		'''
		Changes the Employee classification to an instance of Commissioned
		
		Parameters:
			salary_rate: float
				Employee's salary rate
			commission_rate: float
				Employee's commission rate
		'''
		self.classification = Commissioned(self.emp_string, salary_rate, 
		commission_rate)		
	
	def make_hourly(self, hourly_rate):
		'''
		Changes the Employee classification to an instance of Hourly
		
		Parameters:
			hourly_rate: float
				Employee's hourly rate
		'''
		self.classification = Hourly(self.emp_string, hourly_rate)
	
	def issue_payment(self):
		'''
		Computes employee's pay using classification then outputs to payroll.txt
		'''
		pay = self.classification.compute_pay()
		with open(PAY_LOGFILE, 'a') as f:
			f.write(f"Mailing {pay} to {self._get_firstname()}\
{self._get_lastname()} at {self._get_address()} {self._get_city()}\
{self._get_state()} {self._get_zipcode()}\n")
			
	def get_emp_string(self):
		return self.emp_string
	
	def _get_firstname(self):
		return self._first_name
		
	def _get_lastname(self):
		return self._last_name
		
	def _get_address(self):
		return self._address
		
	def _get_city(self):
		return self._city
		
	def _get_state(self):
		return self._state
		
	def _get_zipcode(self):
		return self._zipcode