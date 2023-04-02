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

    exit_button = ttk.Button(employee_frame, text='Exit',
                             command=lambda: employee_directory(employee, db))
    exit_button.grid(column=6, row=11, sticky=E)
    save_button = Button(employee_frame, text='Save', bg='blue', fg='white',
                         font=('Helvetica', 10), command=update_employee())
    save_button.grid(column=7, row=11, sticky=E)

    sep2 = ttk.Separator(employee_frame, orient=HORIZONTAL)
    sep2.grid(column=1, columnspan=7, row=12, sticky=(W,E))
    employer_info_label = ttk.Label(employee_frame, text='Employer Info')
    employer_info_label.grid(column=1, row=12, sticky='w')

    emp_id_label = ttk.Label(employee_frame, text='Employee ID')
    emp_id_label.grid(column=1, row=13, sticky='w')
    empolyee_id.set(employee.id)
    emp_id_entry = ttk.Entry(employee_frame, textvariable=empolyee_id, state='readonly')
    emp_id_entry.grid(column=1, row=14, sticky='w')

    start_label = ttk.Label(employee_frame, text='Start Date')
    start_label.grid(column=5, row=13)
    employeeStart.set(employee.start_date)
    start_entry = ttk.Entry(employee_frame, textvariable=employeeStart, state='readonly')
    start_entry.grid(column=5, row=14, sticky='w')

    position_label = ttk.Label(employee_frame, text='Position')
    position_label.grid(column=1, row=15, sticky='w')
    title_label = ttk.Label(employee_frame, text='Title')
    title_label.grid(column=1, row=16, sticky='w')
    employeeTitle.set(employee.title)
    title_entry = ttk.Entry(employee_frame, textvariable=employeeTitle)
    title_entry.grid(column=1, row=17, sticky='w')

    department_label = ttk.Label(employee_frame, text='Department')
    department_label.grid(column=5, row=16, sticky='w')
    employeeDepartment.set(employee.dept)
    department_entry = ttk.Entry(employee_frame, textvariable=employeeDepartment)
    department_entry.grid(column=5, row=17, sticky='w')

    emp_archived_label = ttk.Label(employee_frame, text='Archived')
    emp_archived_label.grid(column=1, row=18, sticky='w')
    emp_archived_combo = ttk.Combobox(employee_frame, state='readonly',
                                      textvariable=employeeArchived, width=6)
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

    #employee_pay_method.set(employee.pay_method)
    #if employee_pay_method == 1:
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
    #else:
    #    payment_title = ttk.Label(employee_frame, text='Check by Mail')
    #    payment_title.grid(column=1, row=24)

    #Disable editing for all fields that can be edited by another user but not self
    if user.id == employee.id:
        phone_entry['state'] = 'readonly'
        email_entry['state'] = 'readonly'
        title_entry['state'] = 'readonly'
        department_entry['state'] = 'readonly'
        emp_archived_combo['state'] = 'disabled'
        payroll_class_entry['state'] = 'readonly'

    pad_space()

#Setup navigation bar that sits on the left of the screen
def navigation_bar(locator, navigator: database.Employee):
    """Display the navigation bar on the left of the screen, and setup the navigation buttons"""
    #Adjust root to balance screen around navbar + the main page
    root.columnconfigure(5, weight=1, minsize=50)

    #NavBar frame for all pages
    navigation_frame = ttk.Frame(root, padding="3 3 12 12")
    navigation_frame.grid(column=1, row=1, rowspan = 3, sticky=(N, S))
    navigation_frame['borderwidth'] = 4
    navigation_frame['relief'] = GROOVE

    for i in range(10):
        navigation_frame.rowconfigure(i, minsize=50)

    #NavBar widgets
    if locator == 0:
        directory = ttk.Button(navigation_frame, text='Directory',
                               command=lambda: employee_directory(navigator, db))
        directory.grid(column=0, row=0)
    else:
        back_to_employee = ttk.Button(navigation_frame, text='Employee',
                                      command=lambda: employee_info(navigator))
        back_to_employee.grid(column=0, row=0)

    row_count=1

    #Display priveleged widgets !!!Will fix levels in later testing.
    if int(navigator.permission_level) >= 1:
        admin = ttk.Button(navigation_frame, text='Admin',
                           command=lambda: admin_directory(navigator))
        admin.grid(column=0, row=row_count)
        row_count+=1
    if int(navigator.permission_level) >= 1:
        payroll = ttk.Button(navigation_frame, text='Payroll',
                             command=lambda: payroll_page(navigator))
        payroll.grid(column=0, row=row_count)
        row_count+=1
    if int(navigator.permission_level) >= 1:
        emp_report = ttk.Button(navigation_frame, text='Employee\nReport',
                                command=lambda: employee_report(navigator))
        emp_report.grid(column=0, row=row_count)


    logout_button = ttk.Button(navigation_frame, text='Logout', command=logout)
    logout_button.grid(column=0, row=9, sticky=S)

#Display employee directory
def employee_directory(employee, data):
    """Display a list of the employees, display results of search to limit who is displayed"""
    clean_screen()

    navigation_bar(1, employee)

    #Main directory frame
    direct_frame = ttk.Frame(root, padding="3 3 12 12")
    direct_frame.grid(column=2, row=1, columnspan=3, rowspan=3)
    direct_frame['borderwidth'] = 4
    direct_frame['relief'] = GROOVE
    direct_frame.grid_rowconfigure(0, weight=1)
    direct_frame.grid_columnconfigure(0, weight=1)
    for i in range(10):
        direct_frame.columnconfigure(i, minsize=30)

    #Widgets that occupy the page

    search_label = ttk.Label(direct_frame, text='Search')
    search_label.grid(column=1, row=0, sticky='w')

    search_entry = ttk.Entry(direct_frame, textvariable='Search')
    search_entry.grid(column=1, row=1, columnspan=3, sticky=(W, E))

    search_var = StringVar(direct_frame, 'Employee ID')
    search_combo = ttk.Combobox(direct_frame,  state='readonly', textvariable=search_var)
    search_combo.grid(column=4, row=1)
    search_combo['values']=('Employee ID', 'First Name', 'Last Name', 'Position')

    search_image = PhotoImage(file='search.png')
    search_button = ttk.Button(direct_frame, image=search_image, command=search)
    reference_label= ttk.Label(image=search_image)
    reference_label.image = search_image
    search_button.grid(column=5, row=1)

    slide_canvas = Canvas(direct_frame)
    slide_canvas.grid(column=1, row=6, sticky='news')

    sub_frame = ttk.Frame(slide_canvas)
    sub_frame.grid(column=0, columnspan=9, row=2, sticky=(N, S, E, W))
    sub_frame['borderwidth'] = 4
    sub_frame['relief'] = GROOVE
    for i in range(17):
        sub_frame.columnconfigure(i, minsize=30)


    arch_label = ttk.Label(sub_frame, text='Archived')
    arch_label.grid(column=0, row=0)
    first_name_label = ttk.Label(sub_frame, text='First Name')
    first_name_label.grid(column=2, columnspan=2, row=0)
    last_name_label = ttk.Label(sub_frame, text='Last Name')
    last_name_label.grid(column=5, columnspan=2, row=0)
    id_label = ttk.Label(sub_frame, text='Employee ID')
    id_label.grid(column=8, row=0)
    title_label = ttk.Label(sub_frame, text='Job Title')
    title_label.grid(column=10, row=0)
    phone_label = ttk.Label(sub_frame, text='Phone Number')
    phone_label.grid(column=12, columnspan=3, row=0)

    row_count = 1
    #loop should iterate through array of employees current loop structure for testing layout only
    horizon_sep = []
    for emp in data.employees:
        horizon_sep.append(ttk.Separator(sub_frame, orient=HORIZONTAL)
                           .grid(column=0, columnspan=17, row=row_count, sticky=(W, E)))
        row_count += 1

        employee_archive = emp.archived
        archived_check = ttk.Checkbutton(sub_frame, onvalue='True', offvalue='False',
                                         variable=employee_archive)
        archived_check.grid(column=0, row=row_count)

        first_name_label = ttk.Label(sub_frame, text=emp.first_name)
        first_name_label.grid(column=2, row=row_count, sticky=W)

        last_name_label = ttk.Label(sub_frame, text=emp.last_name)
        last_name_label.grid(column=5, row=row_count, sticky=W)

        id_label = ttk.Label(sub_frame, text=emp.id)
        id_label.grid(column=8, row=row_count, sticky=W)

        title_label = ttk.Label(sub_frame, text=emp.title)
        title_label.grid(column=10, row=row_count, sticky=W)

        phone_label = ttk.Label(sub_frame, text=emp.office_phone)
        phone_label.grid(column=12, row=row_count)

        view_button = ttk.Button(sub_frame, text='View',
                                 command=lambda: employee_info(db.find_employees(None, emp.id)))
        view_button.grid(column=16, row=row_count)
        row_count += 1

    long_view = ttk.Scrollbar(slide_canvas, command=slide_canvas.yview)
    long_view.grid(column=9, row=0, rowspan=row_count, sticky='ns')
    slide_canvas.configure(yscrollcommand=long_view.set)


    #Separators down column 1, 4, 7, 9, 11, 15
    vert_sep_1 = ttk.Separator(sub_frame, orient=VERTICAL)
    vert_sep_1.grid(column=1, row=0, sticky=(N, S))

    vert_sep_4 = ttk.Separator(sub_frame, orient=VERTICAL)
    vert_sep_4.grid(column=4, row=0, sticky=(N, S))

    vert_sep_7 = ttk.Separator(sub_frame, orient=VERTICAL)
    vert_sep_7.grid(column=7, row=0, sticky=(N, S))

    vert_sep_9 = ttk.Separator(sub_frame, orient=VERTICAL)
    vert_sep_9.grid(column=9, row=0, sticky=(N, S))

    vert_sep_11 = ttk.Separator(sub_frame, orient=VERTICAL)
    vert_sep_11.grid(column=11, row=0, sticky=(N, S))

    vert_sep_15 = ttk.Separator(sub_frame, orient=VERTICAL)
    vert_sep_15.grid(column=15, row=0, sticky=(N, S))


    pad_space()

#Admin Page !!!Main bit of page can be copied from the directory function
def admin_directory(admin_user):
    """Display Admin Page, main unique feature is the add employee button which may require its own
    page or pop-up screen since some employee attributes are not currently displayed or used"""
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
    global user
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
        for inner_child in child.winfo_children():
            inner_child.grid_configure(padx=5, pady=5)

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

    #It seeems that pay_method doesn't exist as an employee attribute
    #if employee_pay_method != changed_employee.pay_method:
    #    changed_employee.pay_method = employee_pay_method
    #if employee_pay_method == 1:
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
