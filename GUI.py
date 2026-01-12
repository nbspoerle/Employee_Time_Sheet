import Excel_Data
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

# -------------------------
# Hours Worked (ROOT uses PACK)
# -------------------------
hours_worked = StringVar()

hours_worked_label = Label(root, text="Hours Worked")
hours_worked_label.pack(pady=10)

hours_worked_entry = Entry(root, textvariable=hours_worked)
hours_worked_entry.pack(pady=10)

# -------------------------
# Dropdown (ROOT uses PACK)
# -------------------------
selection_emp = StringVar(value="No employees yet")

dropdown = OptionMenu(root, selection_emp, "No employees yet")
dropdown.pack(pady=10)

def refresh_dropdown():
    menu = dropdown["menu"]
    menu.delete(0, "end")

    if not employees:
        selection_emp.set("No employees yet")
        menu.add_command(
            label="No employees yet",
            command=lambda v="No employees yet": selection_emp.set(v)
        )
    else:
        # Display names
        first_item = employees[0].first
        selection_emp.set(first_item)

        for emp in employees:
            label = emp.first
            menu.add_command(label=label, command=lambda v=label: selection_emp.set(v))

# -------------------------
# Calendar (ROOT uses PACK)
# -------------------------
cal = Calendar(root, selectmode='day', year=today.year, month=today.month, day=today.day)
cal.pack(pady=10)

date_label = Label(root, text="")
date_label.pack(pady=10)

def grab_date():
    date_label.config(text="Selected Date is: " + cal.get_date())

Button(root, text="Get Date", command=grab_date).pack(pady=10)

# -------------------------
# Add Employee Popup (TOPLEVEL uses GRID)
# -------------------------
def add_employee_window():
    win = Toplevel(root)
    win.title("Add Employee")
    win.geometry("500x250")

    Label(win, text="First Name").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    first_entry = Entry(win)
    first_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(win, text="PTO").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    pto_entry = Entry(win)
    pto_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(win, text="Pay").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    pay_entry = Entry(win)
    pay_entry.grid(row=2, column=1, padx=10, pady=10)

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

            refresh_dropdown()  # update dropdown choices
            win.destroy()

        except ValueError:
            messagebox.showerror("Error", "PTO and Pay must be numbers")

    Button(win, text="Save", command=save_employee).grid(row=3, column=0, padx=10, pady=15)
    Button(win, text="Cancel", command=win.destroy).grid(row=3, column=1, padx=10, pady=15)

# IMPORTANT: This button is on ROOT, so it must use PACK (not grid)
Button(root, text="Add Employee", command=add_employee_window).pack(pady=10)

root.mainloop()
