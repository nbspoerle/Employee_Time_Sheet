from tkinter import *
from tkinter import messagebox
from AddEmployee import Employee

employees = []

#Create the window
root = Tk()

#Title the window
root.title("Employee Time Sheet")

#give window size
root.geometry("500x500")

def add_employee_window():
    #Creates Popup
    win = Toplevel(root)
    win.title("Employee Time Sheet")
    win.geometry("500x500")

    #Creates entry box to store input
    Label(win, text="First Name").grid(row=0, column=0)
    first_entry = Entry(win)
    first_entry.grid(row=0, column=1)

    Label(win, text="PTO").grid(row=1, column=0)
    pto_entry = Entry(win)
    pto_entry.grid(row=1, column=1)

    Label(win, text = "Pay").grid(row=2, column=0)
    pay_entry = Entry(win)
    pay_entry.grid(row=2, column=1)

    def save_employee():
        #Error Handling for invalid input
        try:
            #Reads the users input
            first = first_entry.get()
            pto = float(pto_entry.get())
            pay = float(pay_entry.get())

            emp = Employee(first, pto, pay)  #create object
            employees.append(emp)  #save to list

            print(f"Added: {emp.first}, PTO={emp.pto}, Pay={emp.pay}")
            win.destroy()

        except ValueError:
            messagebox.showerror("Error", "PTO and Pay must be numbers")

    Button(win, text="Save", command=save_employee).grid(row=3, column=0, pady=10)
    Button(win, text="Cancel", command=win.destroy).grid(row=3, column=1, pady=10)


Button(root, text="Add Employee", command=add_employee_window).grid(row=0, column=0, padx=20, pady=20)

root.mainloop()