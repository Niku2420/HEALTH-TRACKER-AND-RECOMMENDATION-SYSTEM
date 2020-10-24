from bmi import *
import tkinter


def calculate():
    user = Patient(weight=float(weight_entry.get()),
                   height=float(height_entry.get()))
    bmi_label.configure(text="Your BMI is " +
                             str(round(user.calculate_bmi(), 2))
                             + " which is "
                             + user.bmi_analysis() + ".")

interface = tkinter.Tk()
interface.title("HEALTH TRACKER AND RECOMMENDATION SYSTEM")
interface.minsize(800, 500)

# declare labels
height_label = tkinter.Label(text="Height (m)")
weight_label = tkinter.Label(text="Weight (Kg)")
steps_label = tkinter.Label(text="Steps (units)")
bmi_label = tkinter.Label()

# declare entry boxes
height_entry = tkinter.Entry(justify="right")
weight_entry = tkinter.Entry(justify="right")
steps_entry = tkinter.Entry(justify="right")

# declare buttons
calculate_button = tkinter.Button(text="evaluate", command=calculate)

# place widgets on grid
height_label.grid(row=0, column=0, padx=30, pady=30)
height_entry.grid(row=0, column=1, padx=30, pady=30)
weight_label.grid(row=1, column=0, padx=30, pady=30)
weight_entry.grid(row=1, column=1, padx=30, pady=30)
steps_label.grid(row=2, column=0, padx=30, pady=30)
steps_entry.grid(row=2, column=1, padx=30, pady=30)
bmi_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
calculate_button.grid(row=5, column=1, padx=10, pady=10)

# interface loop
tkinter.mainloop()