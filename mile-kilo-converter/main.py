from tkinter import *

FONT = ("Arial", 16, "normal")


def calculate():
    miles = float(miles_value.get())  # get() type: str
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)

miles_value = Entry(width=7)
miles_value.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is eqaul to", font=FONT)
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0", font=FONT)
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=FONT)
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
