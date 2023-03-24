from tkinter import *
from tkinter import ttk

#Setup root
root = Tk()
root.title("UVU Employee Services")

#Setup alternate style
style = ttk.Style()
style.configure('link.TLabel', foreground='blue')
style.layout('login.TButton', )

#Funtions to display each page.
#First page is the login page
def DisplayLogin():

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
    logo = ttk.Label(loginFrame, text='Cool Logo (need image)').grid(column=3,row=0)
    title = ttk.Label(loginFrame, text='Sign In').grid(column=3, row=1)
    idLabel = ttk.Label(loginFrame, text="Employee ID").grid(column=2, sticky=W)
    idEntry = ttk.Entry(loginFrame, textvariable='employeeID').grid(column=2, columnspan=3, sticky=(W, E))
    pssLabel = ttk.Label(loginFrame, text="Password").grid(column=2, sticky=W)
    pssEntry = ttk.Entry(loginFrame, textvariable="password").grid(column=2, columnspan=3, sticky=(W, E))
    login = ttk.Button(loginFrame, text="Login", style='login.TButton', command=Login).grid(column=4, sticky=E)

    #add minimum padding to all of the widgets
    for child in loginFrame.winfo_children():
        child.grid_configure(padx=5, pady=5)

#Second page is employee info
def EmployeeInfo():
    #main frame for employee info page
    employeeFrame = ttk.Frame(root, padding="3 3 12 12")
    employeeFrame.grid(column=1, row=1, columnspan=3, rowspan=3)
    employeeFrame['borderwidth'] = 4
    employeeFrame['relief'] = GROOVE
    for i in range(9):
        employeeFrame.columnconfigure(i, minsize=30)
        employeeFrame.rowconfigure(i, minsize=30)

    #setup the widgets
    title = ttk.Label(employeeFrame, text='Employee').grid(column=4, row=0)

#Setup navigation bar that sits on the left of the screen
def NavigationBar():
    #NavBar frame for all pages
    navigationFrame = ttk.Frame(root, padding="3 3 12 12")
    navigationFrame.grid(column=0, row=0, rowspan = 5)
    navigationFrame['borderwidth'] = 4
    navigationFrame['relief'] = GROOVE

    for i in range(5):
        navigationFrame.rowconfigure(i, minsize=50)

    #NavBar widgets
    logout = ttk.Button(navigationFrame, text='Logout', command=Logout).grid(column=0, row=4)

#Login process deletes login page then calls employee info to construct that page.
def Login(empid = 0, password = 'a'):
    for child in root.winfo_children():
        child.destroy()

    NavigationBar()
    EmployeeInfo()

def Logout():
    for child in root.winfo_children():
        child.destroy()

    DisplayLogin()

#Display login is called on program start
DisplayLogin()

#mainloop is required for the program to continue until user exits
root.mainloop()

