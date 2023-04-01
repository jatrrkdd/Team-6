from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import math
import os
import database

"""
    The following instanciation of the database is for testing to make sure I understand
    how to properly call all of the attributes and functions necessary to adapt my code
    to prepare for integration.
"""
db = database.Database(None,"")

#Setup root
root = Tk()
root.title("UVU Employee Services")

#Setup alternate style
style = ttk.Style()
style.configure('small.TLabel', font=('Helvetica', 7))

"""
    Initialization of various variables that keep getting garbage collected early
"""
currEmployee = None
employeeID = StringVar()
password = StringVar()
employeeFirstName = StringVar()
employeeLastName = StringVar()
employeePhone = StringVar()
employeeEmail = StringVar()
employeeStreet = StringVar()
employeeCity = StringVar()
employeeState = StringVar()
employeeZip = StringVar()
employeeDOB = StringVar()
employeeStart = StringVar()
employeeTitle = StringVar()
employeeDepartment = StringVar()

"""
    Basic trace function, currently does nothing except exist as part of the
    trace_add calls for the diffent textvariables that need to be managed.
"""
def BasicCallback(var, index, mode):
    return 0

#Funtions to display each page.
#First page is the login page
def DisplayLogin():
    CleanScreen()

    #Setup the outer frame for the login page
    loginFrame = ttk.Frame(root, padding="3 3 12 12")
    loginFrame.grid(column=1, row=1, columnspan=3, rowspan=3)
    loginFrame['borderwidth'] = 4
    loginFrame['relief'] = GROOVE

    root.columnconfigure(0, weight=1, minsize=50)
    root.rowconfigure(0, weight=1, minsize=50)
    root.columnconfigure(1, weight=1, minsize=50)
    root.rowconfigure(1, weight=1, minsize=50)
    root.columnconfigure(2, weight=1, minsize=50)
    root.rowconfigure(2, weight=1, minsize=50)
    root.columnconfigure(3, weight=1, minsize=50)
    root.rowconfigure(3, weight=1, minsize=50)
    root.columnconfigure(4, weight=1, minsize=50)
    root.rowconfigure(4, weight=1, minsize=50)
    root.columnconfigure(5, weight=1, minsize=00)

    loginFrame.columnconfigure(0, minsize=50)
    loginFrame.rowconfigure(0, minsize=170)
    loginFrame.columnconfigure(1, minsize=50)
    loginFrame.rowconfigure(1, minsize=30)
    loginFrame.columnconfigure(2, minsize=50)
    loginFrame.rowconfigure(2, minsize=30)
    loginFrame.columnconfigure(3, minsize=50)
    loginFrame.rowconfigure(3, minsize=30)
    loginFrame.columnconfigure(4, minsize=50)
    loginFrame.rowconfigure(4, minsize=30)
    loginFrame.columnconfigure(5, minsize=50)
    loginFrame.rowconfigure(5, minsize=30)
    loginFrame.columnconfigure(6, minsize=50)
    loginFrame.rowconfigure(6, minsize=30)

    #Setup all of the necessary widgets
    logo = ttk.Label(loginFrame, text='Cool Logo (need image)')
    logo.grid(column=3,row=0)
    title = ttk.Label(loginFrame, text='Sign In')
    title.grid(column=3, row=1)
    idLabel = ttk.Label(loginFrame, text="Employee ID")
    idLabel.grid(column=2, sticky=W)
    idEntry = ttk.Entry(loginFrame, textvariable=employeeID)
    employeeID.trace_add('write', BasicCallback)
    idEntry.grid(column=2, columnspan=3, sticky=(W, E))
    pssLabel = ttk.Label(loginFrame, text="Password")
    pssLabel.grid(column=2, sticky=W)
    pssEntry = ttk.Entry(loginFrame, textvariable=password, show="*")
    password.trace_add('write', BasicCallback)
    pssEntry.grid(column=2, columnspan=3, sticky=(W, E))
    login = Button(loginFrame, text="Login", bg='blue', fg='white', font=('Helvetica', 10), command=lambda: Login(employeeID.get(), password.get()))
    login.grid(column=4, sticky=E)

    PadSpace()

#Second page is employee info !!!Currently doesn't actually use the argument needs database connection
def EmployeeInfo(employee: database.Employee):
    global currEmployee

    CleanScreen()

    NavigationBar(0, employee)

    #main frame for employee info page
    employeeFrame = ttk.Frame(root, padding="3 3 12 12")
    employeeFrame.grid(column=2, row=1, columnspan=3, rowspan=3)
    employeeFrame['borderwidth'] = 4
    employeeFrame['relief'] = GROOVE
    for i in range(9):
        employeeFrame.columnconfigure(i, minsize=30)
    for i in range(13):
        employeeFrame.rowconfigure(i, minsize=30)

    #setup the widgets
    title = ttk.Label(employeeFrame, text='Employee Information')
    title.grid(column=5, row=0)
    sep1 = ttk.Separator(employeeFrame, orient=HORIZONTAL)
    sep1.grid(column=1, columnspan=7, row=1, sticky=(W, E))

    empFirstNameLabel = ttk.Label(employeeFrame, text='First Name')
    empFirstNameLabel.grid(column=1, row=2, sticky=W)
    employeeFirstName.set(employee.first_name)
    empFirstNameEntry = ttk.Entry(employeeFrame, textvariable=employeeFirstName)
    employeeFirstName.trace_add('write', BasicCallback)
    empFirstNameEntry.grid(column=1, row=3, columnspan=3, sticky=W)
    empLastNameLabel = ttk.Label(employeeFrame, text='Last Name')
    empLastNameLabel.grid(column=5, row=2, sticky=W)
    employeeLastName.set(employee.last_name)
    empLastNameEntry = ttk.Entry(employeeFrame, textvariable=employeeLastName)
    employeeLastName.trace_add('write', BasicCallback)
    empLastNameEntry.grid(column=5, row=3, columnspan=3, sticky=W)

    empPhoneLabel = ttk.Label(employeeFrame, text='Phone #')
    empPhoneLabel.grid(column=1, row=4, sticky=W)
    employeePhone.set(employee.office_phone)
    empPhoneEntry = ttk.Entry(employeeFrame, textvariable=employeePhone)
    empPhoneEntry.grid(column=1, row=5, sticky=W)
    empEmailLabel = ttk.Label(employeeFrame, text='Email')
    empEmailLabel.grid(column=5, row=4, sticky=W)
    employeeEmail.set(employee.email)
    empEmailEntry = ttk.Entry(employeeFrame, textvariable=employeeEmail)
    empEmailEntry.grid(column=5, row=5, sticky=W)

    empAddressLabel = ttk.Label(employeeFrame, text='Address')
    empAddressLabel.grid(column=1, row=6, sticky=W)
    empStreetLabel = ttk.Label(employeeFrame, text='Street Address', style='small.TLabel')
    empStreetLabel.grid(column=1, row=7, sticky=W)
    employeeStreet.set(employee.address)
    empStreetEntry = ttk.Entry(employeeFrame, textvariable=employeeStreet)
    empStreetEntry.grid(column=1, row=8, columnspan=3, sticky=W)
    empCityLabel = ttk.Label(employeeFrame, text='City', style='small.TLabel')
    empCityLabel.grid(column=4, row=7, sticky=W)
    employeeCity.set(employee.city)
    empCityEntry = ttk.Entry(employeeFrame, textvariable=employeeCity)
    empCityEntry.grid(column=4, row=8, columnspan=2, sticky=W)
    empStateLabel = ttk.Label(employeeFrame, text='State', style='small.TLabel')
    empStateLabel.grid(column=6, row=7, sticky=W)
    employeeState.set(employee.state)
    empStateEntry = ttk.Entry(employeeFrame, textvariable=employeeState)
    empStateEntry.grid(column=6, row=8, sticky=W)
    empZipLabel = ttk.Label(employeeFrame, text='Zip Code', style='small.TLabel')
    empZipLabel.grid(column=7, row=7, sticky=W)
    employeeZip.set(employee.zip)
    empZipEntry = ttk.Entry(employeeFrame, textvariable=employeeZip)
    empZipEntry.grid(column=7, row=8, sticky=W)

    empDobLabel = ttk.Label(employeeFrame, text="Date of Birth")
    empDobLabel.grid(column=1, row=9)
    employeeDOB.set(employee.DOB)
    empDobEntry = ttk.Entry(employeeFrame, textvariable=employeeDOB, state='readonly')
    empDobEntry.grid(column=1, row=10)

    empExitButton = ttk.Button(employeeFrame, text='Exit', command=lambda: EmployeeDirectory(employee))
    empExitButton.grid(column=6, row=11, sticky=E)
    empSaveButton = Button(employeeFrame, text='Save', bg='blue', fg='white', font=('Helvetica', 10))
    empSaveButton.grid(column=7, row=11, sticky=E)

    sep2 = ttk.Separator(employeeFrame, orient=HORIZONTAL)
    sep2.grid(column=1, columnspan=7, row=12, sticky=(W,E))
    employerInfoLabel = ttk.Label(employeeFrame, text='Employer Info')
    employerInfoLabel.grid(column=1, row=12, sticky=W)

    empIDLabel = ttk.Label(employeeFrame, text='Employee ID')
    empIDLabel.grid(column=1, row=13, sticky=W)
    employeeID.set(employee.id)
    empIDEntry = ttk.Entry(employeeFrame, textvariable=employeeID, state='readonly')
    empIDEntry.grid(column=1, row=14, sticky=W)

    empStartLabel = ttk.Label(employeeFrame, text='Start Date')
    empStartLabel.grid(column=5, row=13)
    employeeStart.set(employee.start_date)
    empStartEntry = ttk.Entry(employeeFrame, textvariable=employeeStart, state='readonly')
    empStartEntry.grid(column=5, row=14, sticky=W)

    empPositionLabel = ttk.Label(employeeFrame, text='Position')
    empPositionLabel.grid(column=1, row=15, sticky=W)
    empTitleLabel = ttk.Label(employeeFrame, text='Title')
    empTitleLabel.grid(column=1, row=16, sticky=W)
    employeeTitle.set(employee.title)
    empTitleEntry = ttk.Entry(employeeFrame, textvariable=employeeTitle)
    empTitleEntry.grid(column=1, row=17, sticky=W)

    empDepartmentLabel = ttk.Label(employeeFrame, text='Department')
    empDepartmentLabel.grid(column=5, row=16, sticky=W)
    employeeDepartment.set(employee.dept)
    empDepartmentEntry = ttk.Entry(employeeFrame, textvariable=employeeDepartment)
    empDepartmentEntry.grid(column=5, row=17, sticky=W)

    empArchivedLabel = ttk.Label(employeeFrame, text='Archived')
    empArchivedLabel.grid(column=1, row=18)

    """ 
        Disable editing for all fields that can be edited by another user but not self
    """
    if currEmployee.id == employee.id:
        empPhoneEntry['state'] = 'readonly'
        empEmailEntry['state'] = 'readonly'
        empTitleEntry['state'] = 'readonly'
        empDepartmentEntry['state'] = 'readonly'

    PadSpace()

#Setup navigation bar that sits on the left of the screen
def NavigationBar(locator, currEmployee: database.Employee):
    #Adjust root to balance screen around navbar + the other page
    root.columnconfigure(5, weight=1, minsize=50)
    #NavBar frame for all pages
    navigationFrame = ttk.Frame(root, padding="3 3 12 12")
    navigationFrame.grid(column=1, row=1, rowspan = 3, sticky=(N, S))
    navigationFrame['borderwidth'] = 4
    navigationFrame['relief'] = GROOVE

    for i in range(10):
        navigationFrame.rowconfigure(i, minsize=50)

    #NavBar widgets
    if locator == 0:
        directory = ttk.Button(navigationFrame, text='Directory', command=lambda: EmployeeDirectory(currEmployee))
        directory.grid(column=0, row=0)
    else:
        backToEmployee = ttk.Button(navigationFrame, text='Employee', command=lambda: EmployeeInfo(currEmployee))
        backToEmployee.grid(column=0, row=0)

    rowCount=1

    #Display priveleged widgets
    """
        To my understanding there should be three levels of permissions, but I am not sure and all of the
        test data are either 0 or 1 so for now I will proceed with only the one level of permission check
        though I will repeat the check for easier changes to it later.
    """
    if int(currEmployee.permission_level) >= 1:
        admin = ttk.Button(navigationFrame, text='Admin', command=lambda: AdminDirectory(currEmployee))
        admin.grid(column=0, row=rowCount)
        rowCount+=1
    if int(currEmployee.permission_level) >= 1:
        payroll = ttk.Button(navigationFrame, text='Payroll', command=lambda: PayrollPage(currEmployee))
        payroll.grid(column=0, row=rowCount)
        rowCount+=1
    if int(currEmployee.permission_level) >= 1:
        empReport = ttk.Button(navigationFrame, text='Employee\nReport', command=lambda: EmployeeReport(currEmployee))
        empReport.grid(column=0, row=rowCount)


    logout = ttk.Button(navigationFrame, text='Logout', command=Logout)
    logout.grid(column=0, row=9, sticky=S)

#Display employee directory
def EmployeeDirectory(currEmployee):
    CleanScreen()
    
    NavigationBar(1, currEmployee)
    
    #Main directory frame
    directFrame = ttk.Frame(root, padding="3 3 12 12")
    directFrame.grid(column=2, row=1, columnspan=3, rowspan=3)
    directFrame['borderwidth'] = 4
    directFrame['relief'] = GROOVE
    for i in range(9):
        directFrame.columnconfigure(i, minsize=30)

    searchLabel = ttk.Label(directFrame, text='Search')
    searchLabel.grid(column=1, row=0, sticky=W)

    searchEntry = ttk.Entry(directFrame, textvariable='Search')
    searchEntry.grid(column=1, row=1, columnspan=3, sticky=(W, E))

    searchVar = StringVar(directFrame, 'Employee ID')
    searchCombo = ttk.Combobox(directFrame,  state='readonly', textvariable=searchVar)
    searchCombo.grid(column=4, row=1)
    searchCombo['values']=('Employee ID', 'First Name', 'Last Name', 'Position')

    searchImage = PhotoImage(file='search.png')
    searchButton = ttk.Button(directFrame, image=searchImage, command=Search)
    referenceLabel= ttk.Label(image=searchImage)
    referenceLabel.image = searchImage
    searchButton.grid(column=5, row=1)

    subFrame = ttk.Frame(directFrame, padding="3 3 12 12")
    subFrame.grid(column=0, columnspan=9, row=2, sticky=(N, S, E, W))
    subFrame['borderwidth'] = 4
    subFrame['relief'] = GROOVE
    for i in range(17):
        subFrame.columnconfigure(i, minsize=30)

    archLabel = ttk.Label(subFrame, text='Archived')
    archLabel.grid(column=0, row=0)
    firstNameLabel = ttk.Label(subFrame, text='First Name')
    firstNameLabel.grid(column=2, columnspan=2, row=0)
    lastNameLabel = ttk.Label(subFrame, text='Last Name')
    lastNameLabel.grid(column=5, columnspan=2, row=0)
    idLabel = ttk.Label(subFrame, text='Employee ID')
    idLabel.grid(column=8, row=0)
    titleLabel = ttk.Label(subFrame, text='Job Title')
    titleLabel.grid(column=10, row=0)
    phoneLabel = ttk.Label(subFrame, text='Phone Number')
    phoneLabel.grid(column=12, columnspan=3, row=0)

    rowCount = 1
    #loop should iterate through array of employees current loop structure for testing layout only
    horizonSep = []
    for employee in range(5):
        horizonSep.append(ttk.Separator(subFrame, orient=HORIZONTAL).grid(column=0, columnspan=17, row=rowCount, sticky=(W, E)))
        rowCount += 1

        viewButton = ttk.Button(subFrame, text='View', command=lambda: EmployeeInfo(''))
        viewButton.grid(column=16, row=rowCount)
        rowCount += 1


    #Separators down column 1, 4, 7, 9, 11, 15
    vertSep1 = ttk.Separator(subFrame, orient=VERTICAL)
    vertSep1.grid(column=1, row=0, sticky=(N, S))
    
    vertSep4 = ttk.Separator(subFrame, orient=VERTICAL)
    vertSep4.grid(column=4, row=0, sticky=(N, S))
    
    vertSep7 = ttk.Separator(subFrame, orient=VERTICAL)
    vertSep7.grid(column=7, row=0, sticky=(N, S))
    
    vertSep9 = ttk.Separator(subFrame, orient=VERTICAL)
    vertSep9.grid(column=9, row=0, sticky=(N, S))

    vertSep11 = ttk.Separator(subFrame, orient=VERTICAL)
    vertSep11.grid(column=11, row=0, sticky=(N, S))

    vertSep15 = ttk.Separator(subFrame, orient=VERTICAL)
    vertSep15.grid(column=15, row=0, sticky=(N, S))


    PadSpace()

#Admin Page !!!Main bit of page can be copied from the directory function
def AdminDirectory(currEmployee):
    CleanScreen()

    NavigationBar(0, currEmployee)

    PadSpace()

#Payroll page !!!Main bit can be copied from directory
def PayrollPage(currEmployee):
    CleanScreen()

    NavigationBar(0, currEmployee)

    PadSpace()

#Employee Report page !!!Main bit can be copied from directory
def EmployeeReport(currEmployee):
    CleanScreen()

    NavigationBar(0, currEmployee)

    PadSpace()

#Login process deletes login page then calls employee info to construct that page.
def Login(empID, password):
    global currEmployee
    currEmployee = db.check_login(empID, password)
    
    if currEmployee:    
        EmployeeInfo(currEmployee)

#Logout removes the current user variable, and returns to the login screen
def Logout():
    #Reset login variables
    currEmployee = None
    employeeID.set('')
    password.set('')

    #Display Login page
    DisplayLogin()

#Clean screen function to remove unneeded widgets
def CleanScreen():
    for child in root.winfo_children():
        child.destroy()

#PadSpace to quickly add a minimum amount of space between many widgets  
def PadSpace():
    #add minimum padding to all of the widgets
    for child in root.winfo_children():
        for innerChild in child.winfo_children():
            innerChild.grid_configure(padx=5, pady=5)

#Search employee directory based on currently selected criteria
def Search():
    return 0

#Display login is called on program start
DisplayLogin()

#mainloop is required for the program to continue until user exits
root.mainloop()

