"""GUI module for employee directory and payroll management system"""
from tkinter import *
from tkinter import ttk
import database


#    The following instanciation of the database is for testing to make sure I understand
#    how to properly call all of the attributes and functions necessary to adapt my code
#    to prepare for integration.
db = database.Database(None,"")

#Setup root
root = Tk()
root.title("UVU Employee Services")

#Setup alternate style
style = ttk.Style()
style.configure('small.TLabel', font=('Helvetica', 7))


#Initialization of various variables that keep getting garbage collected early
#User is not a constant
user = None
empolyee_id = StringVar()
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
employeeArchived = StringVar(value='False')
employee_classification = StringVar()
employee_pay_amount = StringVar()
employee_pay_method = StringVar()
employee_routing = StringVar()
employee_account_num = StringVar()


def basic_callback(var, index, mode):
    """Callback exists just to help tracefunctions work properly, no further 
    functionality is currently needed"""

    return 0

#Funtions to display each page.
#First page is the login page
def display_login():
    """Function clears the root, then displays the login page and implents the trace calls and
    and commands needed for the page to function"""
    clean_screen()

    #Setup the outer frame for the login page
    login_frame = ttk.Frame(root, padding="3 3 12 12")
    login_frame.grid(column=1, row=1, columnspan=3, rowspan=3)
    login_frame['borderwidth'] = 4
    login_frame['relief'] = 'groove'

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

    login_frame.columnconfigure(0, minsize=50)
    login_frame.rowconfigure(0, minsize=170)
    login_frame.columnconfigure(1, minsize=50)
    login_frame.rowconfigure(1, minsize=30)
    login_frame.columnconfigure(2, minsize=50)
    login_frame.rowconfigure(2, minsize=30)
    login_frame.columnconfigure(3, minsize=50)
    login_frame.rowconfigure(3, minsize=30)
    login_frame.columnconfigure(4, minsize=50)
    login_frame.rowconfigure(4, minsize=30)
    login_frame.columnconfigure(5, minsize=50)
    login_frame.rowconfigure(5, minsize=30)
    login_frame.columnconfigure(6, minsize=50)
    login_frame.rowconfigure(6, minsize=30)

    #Setup all of the necessary widgets
    logo = ttk.Label(login_frame, text='Cool Logo (need image)')
    logo.grid(column=3,row=0)
    title = ttk.Label(login_frame, text='Sign In')
    title.grid(column=3, row=1)
    id_label = ttk.Label(login_frame, text="Employee ID")
    id_label.grid(column=2, sticky='w')
    id_entry = ttk.Entry(login_frame, textvariable=empolyee_id)
    empolyee_id.trace_add('write', basic_callback)
    id_entry.grid(column=2, columnspan=3, sticky='we')
    pss_label = ttk.Label(login_frame, text="Password")
    pss_label.grid(column=2, sticky='w')
    pss_entry = ttk.Entry(login_frame, textvariable=password, show="*")
    password.trace_add('write', basic_callback)
    pss_entry.grid(column=2, columnspan=3, sticky='we')
    login_button = Button(login_frame, text="Login", bg='blue', fg='white', font=('Helvetica', 10))
    login_button['command'] =lambda: login(empolyee_id.get(), password.get())
    login_button.grid(column=4, sticky='e')

    pad_space()

#Second page is employee info
def employee_info(employee: database.Employee):
    """Clear screen, then display the employee info page.
    After successful login the app defaults to this page displaying the user's information"""

    clean_screen()

    navigation_bar(0, employee)

    #main frame for employee info page
    employee_frame = ttk.Frame(root, padding="3 3 12 12")
    employee_frame.grid(column=2, row=1, columnspan=3, rowspan=3)
    employee_frame['borderwidth'] = 4
    employee_frame['relief'] = GROOVE
    for i in range(9):
        employee_frame.columnconfigure(i, minsize=30)
    for i in range(13):
        employee_frame.rowconfigure(i, minsize=30)

    #setup the widgets
    title = ttk.Label(employee_frame, text='Employee Information')
    title.grid(column=5, row=0)
    sep1 = ttk.Separator(employee_frame, orient=HORIZONTAL)
    sep1.grid(column=1, columnspan=7, row=1, sticky=(W, E))

    first_name_label = ttk.Label(employee_frame, text='First Name')
    first_name_label.grid(column=1, row=2, sticky='w')
    employeeFirstName.set(employee.first_name)
    first_name_entry = ttk.Entry(employee_frame, textvariable=employeeFirstName)
    employeeFirstName.trace_add('write', basic_callback)
    first_name_entry.grid(column=1, row=3, columnspan=3, sticky='w')
    last_name_label = ttk.Label(employee_frame, text='Last Name')
    last_name_label.grid(column=5, row=2, sticky='w')
    employeeLastName.set(employee.last_name)
    last_name_entry = ttk.Entry(employee_frame, textvariable=employeeLastName)
    employeeLastName.trace_add('write', basic_callback)
    last_name_entry.grid(column=5, row=3, columnspan=3, sticky='w')

    phone_label = ttk.Label(employee_frame, text='Phone #')
    phone_label.grid(column=1, row=4, sticky='w')
    employeePhone.set(employee.office_phone)
    phone_entry = ttk.Entry(employee_frame, textvariable=employeePhone)
    phone_entry.grid(column=1, row=5, sticky='w')
    email_label = ttk.Label(employee_frame, text='Email')
    email_label.grid(column=5, row=4, sticky='w')
    employeeEmail.set(employee.email)
    email_entry = ttk.Entry(employee_frame, textvariable=employeeEmail)
    email_entry.grid(column=5, row=5, sticky='w')

    address_label = ttk.Label(employee_frame, text='Address')
    address_label.grid(column=1, row=6, sticky='w')
    street_label = ttk.Label(employee_frame, text='Street Address', style='small.TLabel')
    street_label.grid(column=1, row=7, sticky='w')
    employeeStreet.set(employee.address)
    street_entry = ttk.Entry(employee_frame, textvariable=employeeStreet)
    street_entry.grid(column=1, row=8, columnspan=3, sticky='w')
    city_label = ttk.Label(employee_frame, text='City', style='small.TLabel')
    city_label.grid(column=4, row=7, sticky='w')
    employeeCity.set(employee.city)
    city_entry = ttk.Entry(employee_frame, textvariable=employeeCity)
    city_entry.grid(column=4, row=8, columnspan=2, sticky='w')
    state_label = ttk.Label(employee_frame, text='State', style='small.TLabel')
    state_label.grid(column=6, row=7, sticky='w')
    employeeState.set(employee.state)
    state_entry = ttk.Entry(employee_frame, textvariable=employeeState)
    state_entry.grid(column=6, row=8, sticky='w')
    zip_label = ttk.Label(employee_frame, text='Zip Code', style='small.TLabel')
    zip_label.grid(column=7, row=7, sticky='w')
    employeeZip.set(employee.zip)
    zip_entry = ttk.Entry(employee_frame, textvariable=employeeZip)
    zip_entry.grid(column=7, row=8, sticky='w')

    dob_label = ttk.Label(employee_frame, text="Date of Birth")
    dob_label.grid(column=1, row=9)
    employeeDOB.set(employee.DOB)
    dob_entry = ttk.Entry(employee_frame, textvariable=employeeDOB)
    dob_entry.grid(column=1, row=10)

    exit_button = ttk.Button(employee_frame, text='Exit', command=lambda: employee_directory(employee))
    exit_button.grid(column=6, row=11, sticky=E)
    save_button = Button(employee_frame, text='Save', bg='blue', fg='white', font=('Helvetica', 10), command=update_employee())
    save_button.grid(column=7, row=11, sticky=E)

    sep2 = ttk.Separator(employee_frame, orient=HORIZONTAL)
    sep2.grid(column=1, columnspan=7, row=12, sticky=(W,E))
    employerInfoLabel = ttk.Label(employee_frame, text='Employer Info')
    employerInfoLabel.grid(column=1, row=12, sticky='w')

    empId_label = ttk.Label(employee_frame, text='Employee ID')
    empId_label.grid(column=1, row=13, sticky='w')
    empolyee_id.set(employee.id)
    empId_entry = ttk.Entry(employee_frame, textvariable=empolyee_id, state='readonly')
    empId_entry.grid(column=1, row=14, sticky='w')

    empStartLabel = ttk.Label(employee_frame, text='Start Date')
    empStartLabel.grid(column=5, row=13)
    employeeStart.set(employee.start_date)
    empStartEntry = ttk.Entry(employee_frame, textvariable=employeeStart, state='readonly')
    empStartEntry.grid(column=5, row=14, sticky='w')

    empPositionLabel = ttk.Label(employee_frame, text='Position')
    empPositionLabel.grid(column=1, row=15, sticky='w')
    empTitleLabel = ttk.Label(employee_frame, text='Title')
    empTitleLabel.grid(column=1, row=16, sticky='w')
    employeeTitle.set(employee.title)
    empTitleEntry = ttk.Entry(employee_frame, textvariable=employeeTitle)
    empTitleEntry.grid(column=1, row=17, sticky='w')

    empDepartmentLabel = ttk.Label(employee_frame, text='Department')
    empDepartmentLabel.grid(column=5, row=16, sticky='w')
    employeeDepartment.set(employee.dept)
    empDepartmentEntry = ttk.Entry(employee_frame, textvariable=employeeDepartment)
    empDepartmentEntry.grid(column=5, row=17, sticky='w')

    emp_archived_label = ttk.Label(employee_frame, text='Archived')
    emp_archived_label.grid(column=1, row=18, sticky='w')
    emp_archived_combo = ttk.Combobox(employee_frame, state='readonly', textvariable=employeeArchived, width=6)
    emp_archived_combo['values'] = ('False', 'True')
    emp_archived_combo.grid(column=1, row=19, sticky='w')
    
    sep3 = ttk.Separator(employee_frame, orient=HORIZONTAL)
    sep3.grid(column=1, columnspan=7, row=20, sticky=(W,E))

    payroll_title = ttk.Label(employee_frame, text='Payroll Info')
    payroll_title.grid(column=1, row=21)
    payroll_class_label = ttk.Label(employee_frame, text='Payroll Classification')
    payroll_class_label.grid(column=1, row=22)
    employee_classification.set(employee.classification)
    payroll_class_entry = ttk.Entry(employee_frame, textvariable=employee_classification)
    employee_classification.trace_add('write', basic_callback)
    print(employee_classification)
    payroll_class_entry.grid(column=1,row=23)
    match employee_classification:
        case 1:
            employee_pay_label = ttk.Label(employee_frame, text='Hourly Wage')
            employee_classification.set("Hourly")
            employee_pay_label.grid(column=5, row=22)
            employee_pay_amount.set(employee.hourly)
            employee_pay_entry = ttk.Entry(employee_frame, textvariable=employee_pay_amount)
            employee_pay_entry.grid(column=5, row=23)
        case 3:
            employee_pay_label = ttk.Label(employee_frame, text='Commission')
            employee_classification.set('Commission')
            employee_pay_label.grid(column=5, row=22)
            employee_pay_amount.set(employee.commissioned)
            employee_pay_entry = ttk.Entry(employee_frame, textvariable=employee_pay_amount)
            employee_pay_entry.grid(column=5, row=23)
        case 2:
            employee_pay_label = ttk.Label(employee_frame, text='Yearly Salary')
            employee_classification.set('Salary')
            employee_pay_label.grid(column=5, row=22)
            employee_pay_amount.set(employee.salary)
            employee_pay_entry = ttk.Entry(employee_frame, textvariable=employee_pay_amount)
            employee_pay_entry.grid(column=5, row=23)
        case _:
            print("Payroll information error")

    employee_pay_method.set(employee.pay_method)
    if employee_pay_method == 1:
        payment_title = ttk.Label(employee_frame, text='Bank Information')
        payment_title.grid(column=1, row=24)
        payment_routing_label = ttk.Label(employee_frame, text='Routing #')
        payment_routing_label.grid(column=1, row=25)
        employee_routing.set(employee.route)
        payment_routing_entry = ttk.Entry(employee_frame, textvariable=employee_routing)
        payment_routing_entry.grid(column=1, row=26)
        payment_account_label = ttk.Label(employee_frame, text='Account #')
        payment_account_label.grid(column=5, row=25)
        employee_account_num.set(employee.account)
        payment_account_entry = ttk.Entry(employee_frame, textvariable=employee_account_num)
        payment_account_entry.grid(column=5, row=26)
    else:
        payment_title = ttk.Label(employee_frame, text='Check by Mail')
        payment_title.grid(column=1, row=24)

    #Disable editing for all fields that can be edited by another user but not self
    if user.id == employee.id:
        phone_entry['state'] = 'readonly'
        email_entry['state'] = 'readonly'
        empTitleEntry['state'] = 'readonly'
        empDepartmentEntry['state'] = 'readonly'
        emp_archived_combo['state'] = 'disabled'
        payroll_class_entry['state'] = 'readonly'

    pad_space()

#Setup navigation bar that sits on the left of the screen
def navigation_bar(locator, user: database.Employee):
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
        directory = ttk.Button(navigationFrame, text='Directory', command=lambda: employee_directory(user))
        directory.grid(column=0, row=0)
    else:
        backToEmployee = ttk.Button(navigationFrame, text='Employee', command=lambda: employee_info(user))
        backToEmployee.grid(column=0, row=0)

    rowCount=1

    #Display priveleged widgets
    """
        To my understanding there should be three levels of permissions, but I am not sure and all of the
        test data are either 0 or 1 so for now I will proceed with only the one level of permission check
        though I will repeat the check for easier changes to it later.
    """
    if int(user.permission_level) >= 1:
        admin = ttk.Button(navigationFrame, text='Admin', command=lambda: admin_directory(user))
        admin.grid(column=0, row=rowCount)
        rowCount+=1
    if int(user.permission_level) >= 1:
        payroll = ttk.Button(navigationFrame, text='Payroll', command=lambda: payroll_page(user))
        payroll.grid(column=0, row=rowCount)
        rowCount+=1
    if int(user.permission_level) >= 1:
        empReport = ttk.Button(navigationFrame, text='Employee\nReport', command=lambda: employee_report(user))
        empReport.grid(column=0, row=rowCount)


    logout_button = ttk.Button(navigationFrame, text='Logout', command=logout)
    logout_button.grid(column=0, row=9, sticky=S)

#Display employee directory
def employee_directory(user):
    clean_screen()
    
    navigation_bar(1, user)
    
    #Main directory frame
    directFrame = ttk.Frame(root, padding="3 3 12 12")
    directFrame.grid(column=2, row=1, columnspan=3, rowspan=3)
    directFrame['borderwidth'] = 4
    directFrame['relief'] = GROOVE
    for i in range(9):
        directFrame.columnconfigure(i, minsize=30)

    searchLabel = ttk.Label(directFrame, text='Search')
    searchLabel.grid(column=1, row=0, sticky='w')

    searchEntry = ttk.Entry(directFrame, textvariable='Search')
    searchEntry.grid(column=1, row=1, columnspan=3, sticky=(W, E))

    searchVar = StringVar(directFrame, 'Employee ID')
    searchCombo = ttk.Combobox(directFrame,  state='readonly', textvariable=searchVar)
    searchCombo.grid(column=4, row=1)
    searchCombo['values']=('Employee ID', 'First Name', 'Last Name', 'Position')

    searchImage = PhotoImage(file='search.png')
    searchButton = ttk.Button(directFrame, image=searchImage, command=search)
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
    id_label = ttk.Label(subFrame, text='Employee ID')
    id_label.grid(column=8, row=0)
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

        viewButton = ttk.Button(subFrame, text='View', command=lambda: employee_info(''))
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


    pad_space()

#Admin Page !!!Main bit of page can be copied from the directory function
def admin_directory(admin_user):
    """Display Admin Page, main unique feature is the add employee button which may require its own
    page or pop-up screen since some employee attributes are not currently displayed or used at all"""
    clean_screen()

    navigation_bar(0, admin_user)

    pad_space()

#Payroll page !!!Main bit can be copied from directory
def payroll_page(payroll_user):
    """Display the Payroll Report Page and call the export function"""
    clean_screen()

    navigation_bar(0, payroll_user)

    pad_space()

#Employee Report page !!!Main bit can be copied from directory
def employee_report(curr_employe):
    """Display the Employee Report Page and call the export function"""
    clean_screen()

    navigation_bar(0, curr_employe)

    pad_space()

#Login process deletes login page then calls employee info to construct that page.
def login(user_id, user_password):
    """Validate a correct combination of login information and set global user variable to the
    associated employee from the database."""
    global user
    user = db.check_login(user_id, user_password)

    if user:
        employee_info(user)

#Logout removes the current user variable, and returns to the login screen
def logout():
    """Reset login variables and display the login page."""
    user = None
    empolyee_id.set('')
    password.set('')

    #Display Login page
    display_login()

#Clean screen function to remove unneeded widgets
def clean_screen():
    """Remove all widgets in the root to prepare for a new page to load"""
    for child in root.winfo_children():
        child.destroy()

#Pad_space to quickly add a minimum amount of space between many widgets
def pad_space():
    """add minimum padding to all of the widgets"""
    for child in root.winfo_children():
        for innerChild in child.winfo_children():
            innerChild.grid_configure(padx=5, pady=5)

def update_employee():
    """Save changes made to an employee record"""
    changed_employee = user

    if employeeFirstName != changed_employee.first_name:
        changed_employee.first_name = employeeFirstName
    if employeeLastName != changed_employee.last_name:
        changed_employee.last_name = employeeLastName
    if employeePhone != changed_employee.office_phone:
        changed_employee.office_phone = employeePhone
    if employeeEmail != changed_employee.email:
        changed_employee.email = employeeEmail
    if employeeStreet != changed_employee.address:
        changed_employee.address = employeeStreet
    if employeeCity != changed_employee.city:
        changed_employee.city = employeeCity
    if employeeState != changed_employee.state:
        changed_employee.state = employeeState
    if employeeZip != changed_employee.zip:
        changed_employee.zip = employeeZip
    if employeeDOB != changed_employee.DOB:
        changed_employee.DOB = employeeDOB
    if employeeTitle != changed_employee.title:
        changed_employee.title = employeeTitle
    if employeeDepartment != changed_employee.dept:
        changed_employee.dept = employeeDepartment
    if employeeArchived != changed_employee.archived:
        changed_employee.archived = employeeArchived
    if employee_classification != changed_employee.classification:
        changed_employee.classification = employee_classification

    match employee_classification:
        case 1:
            if employee_pay_amount != changed_employee.hourly:
                changed_employee.hourly = employee_pay_amount
        case 2:
            if employee_pay_amount != changed_employee.salary:
                changed_employee.salary = employee_pay_amount
        case 3:
            if employee_pay_amount != changed_employee.commission:
                changed_employee.commission = employee_pay_amount
        case _:
            print('employee payment update error')

    if employee_pay_method != changed_employee.pay_method:
        changed_employee.pay_method = employee_pay_method
    if employee_pay_method == 1:
        if employee_routing != changed_employee.route:
            changed_employee.route = employee_routing
        if employee_account_num != changed_employee.account:
            changed_employee.account = employee_account_num

    #need to figure out what function to call here
    return 0

#Search employee directory based on currently selected criteria
def search():
    """Call and display the employee search results from database.py"""
    return 0

#Display login is called on program start
display_login()

#mainloop is required for the program to continue until user exits
root.mainloop()
