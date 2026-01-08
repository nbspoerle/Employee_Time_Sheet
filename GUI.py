from tkinter import *
from tkinter import messagebox
from AddEmployee import Employee
from tkcalendar import Calendar
from datetime import date

today = date.today()
employees = []

root = Tk()
root.title("Employee Time Sheet")
root.geometry("500x500")

# Dropdown setup
selection_emp = StringVar(value="No employees yet")

dropdown = OptionMenu(root, selection_emp, "No employees yet")
dropdown.pack(pady=20)

def refresh_dropdown():
    menu = dropdown["menu"]
    menu.delete(0, "end")

    if not employees:
        selection_emp.set("No employees yet")
        menu.add_command(label="No employees yet",
                         command=lambda v="No employees yet": selection_emp.set(v))
    else:
        # Display names
        first_item = employees[0].first
        selection_emp.set(first_item)

        for emp in employees:
            label = emp.first
            menu.add_command(label=label,
                             command=lambda v=label: selection_emp.set(v))

#Calendar
cal = Calendar(root, selectmode='day', year=today.year, month=today.month, day=today.day)
cal.pack(pady=20)

date_label = Label(root, text="")
date_label.pack(pady=20)

def grab_date():
    date_label.config(text="Selected Date is: " + cal.get_date())

Button(root, text="Get Date", command=grab_date).pack(pady=20)

#Add employee popup
def add_employee_window():
    win = Toplevel(root)
    win.title("Add Employee")
    win.geometry("500x500")

    Label(win, text="First Name").grid(row=0, column=0)
    first_entry = Entry(win)
    first_entry.grid(row=0, column=1)

    Label(win, text="PTO").grid(row=1, column=0)
    pto_entry = Entry(win)
    pto_entry.grid(row=1, column=1)

    Label(win, text="Pay").grid(row=2, column=0)
    pay_entry = Entry(win)
    pay_entry.grid(row=2, column=1)

    def save_employee():
        try:
            first = first_entry.get().strip()
            if not first:
                messagebox.showerror("Error", "First Name cannot be empty")
                return

            pto = float(pto_entry.get())
            pay = float(pay_entry.get())

            emp = Employee(first, pto, pay)
            employees.append(emp)

            refresh_dropdown()   #update dropdown choices

            win.destroy()
        except ValueError:
            messagebox.showerror("Error", "PTO and Pay must be numbers")

    Button(win, text="Save", command=save_employee).grid(row=3, column=0, pady=10)
    Button(win, text="Cancel", command=win.destroy).grid(row=3, column=1, pady=10)

Button(root, text="Add Employee", command=add_employee_window).pack(pady=20)

root.mainloop()
