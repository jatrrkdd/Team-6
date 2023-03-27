from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import math
import os

#Setup root
root = Tk()
root.title("UVU Employee Services")

#Setup alternate style
style = ttk.Style()
style.configure('small.TLabel', font=('Helvetica', 7))

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
    idEntry = ttk.Entry(loginFrame, textvariable='employeeID')
    idEntry.grid(column=2, columnspan=3, sticky=(W, E))
    pssLabel = ttk.Label(loginFrame, text="Password")
    pssLabel.grid(column=2, sticky=W)
    pssEntry = ttk.Entry(loginFrame, textvariable="password")
    pssEntry.grid(column=2, columnspan=3, sticky=(W, E))
    login = Button(loginFrame, text="Login", bg='blue', fg='white', font=('Helvetica', 10), command=Login)
    login.grid(column=4, sticky=E)

    PadSpace()

#Second page is employee info !!!Currently doesn't actually use the argument needs database connection
def EmployeeInfo(employee):
    CleanScreen()

    NavigationBar(0)

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
    title = ttk.Label(employeeFrame, text='Employee')
    title.grid(column=5, row=0)
    sep1 = ttk.Separator(employeeFrame, orient=HORIZONTAL)
    sep1.grid(column=1, columnspan=7, row=1, sticky=(W, E))

    empNameLabel = ttk.Label(employeeFrame, text='Name')
    empNameLabel.grid(column=1, row=2, sticky=W)
    empNameEntry = ttk.Entry(employeeFrame, textvariable='employeeName')
    empNameEntry.grid(column=1, row=3, columnspan=3, sticky=W)

    empAddressLabel = ttk.Label(employeeFrame, text='Address')
    empAddressLabel.grid(column=1, row=4, sticky=W)
    empStreetLabel = ttk.Label(employeeFrame, text='Street Address', style='small.TLabel')
    empStreetLabel.grid(column=1, row=5, sticky=W)
    empStreetEntry = ttk.Entry(employeeFrame, textvariable='employeeStreet')
    empStreetEntry.grid(column=1, row=6, columnspan=3, sticky=W)
    empCityLabel = ttk.Label(employeeFrame, text='City', style='small.TLabel')
    empCityLabel.grid(column=4, row=5, sticky=W)
    empCityEntry = ttk.Entry(employeeFrame, textvariable='employeeCity')
    empCityEntry.grid(column=4, row=6, columnspan=2, sticky=W)
    empStateLabel = ttk.Label(employeeFrame, text='State', style='small.TLabel')
    empStateLabel.grid(column=6, row=5, sticky=W)
    empStateEntry = ttk.Entry(employeeFrame, textvariable='employeeCity')
    empStateEntry.grid(column=6, row=6, sticky=W)
    empZipLabel = ttk.Label(employeeFrame, text='Zip Code', style='small.TLabel')
    empZipLabel.grid(column=7, row=5, sticky=W)
    empZipEntry = ttk.Entry(employeeFrame, textvariable='employeeZip')
    empZipEntry.grid(column=7, row=6, sticky=W)

    empPhoneLabel = ttk.Label(employeeFrame, text='Phone #')
    empPhoneLabel.grid(column=1, row=7, sticky=W)
    empPhoneEntry = ttk.Entry(employeeFrame, textvariable='employeePhone')
    empPhoneEntry.grid(column=1, row=8, sticky=W)

    empExitButton = ttk.Button(employeeFrame, text='Exit', command=EmployeeDirectory)
    empExitButton.grid(column=6, row=9, sticky=E)
    empSaveButton = Button(employeeFrame, text='Save', bg='blue', fg='white', font=('Helvetica', 10))
    empSaveButton.grid(column=7, row=9, sticky=E)

    sep2 = ttk.Separator(employeeFrame, orient=HORIZONTAL)
    sep2.grid(column=1, columnspan=7, row=10, sticky=(W,E))
    employerInfoLabel = ttk.Label(employeeFrame, text='Employer Info')
    employerInfoLabel.grid(column=1, row=11, sticky=W)
    empIDLabel = ttk.Label(employeeFrame, text='Employee ID', style='small.TLabel')
    empIDLabel.grid(column=1, row=12, sticky=W)
    empIDEntry = ttk.Entry(employeeFrame, textvariable='employeeID')
    empIDEntry.grid(column=1, row=13, sticky=W)

    PadSpace()

#Setup navigation bar that sits on the left of the screen
def NavigationBar(locator):
    #Adjust root to balance screen around navbar + the other page
    root.columnconfigure(5, weight=1, minsize=50)
    #NavBar frame for all pages
    navigationFrame = ttk.Frame(root, padding="3 3 12 12")
    navigationFrame.grid(column=1, row=1, rowspan = 3, sticky=(N, S))
    navigationFrame['borderwidth'] = 4
    navigationFrame['relief'] = GROOVE

    for i in range(7):
        navigationFrame.rowconfigure(i, minsize=50)

    #NavBar widgets
    if locator == 0:
        directory = ttk.Button(navigationFrame, text='Directory', command=EmployeeDirectory)
        directory.grid(column=0, row=0)
    else:
        backToEmployee = ttk.Button(navigationFrame, text='Employee', command=lambda: EmployeeInfo(''))
        backToEmployee.grid(column=0, row=0)
    logout = ttk.Button(navigationFrame, text='Logout', command=Logout)
    logout.grid(column=0, row=9, sticky=S)

#Display employee directory
def EmployeeDirectory():
    CleanScreen()
    
    NavigationBar(1)
    
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

#Login process deletes login page then calls employee info to construct that page.
def Login(empid = 0, password = 'a'):

    EmployeeInfo('')

#Logout removes the current user variable, and returns to the login screen
def Logout():

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

