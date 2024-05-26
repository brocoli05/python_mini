from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=240, height=240)
window.config(padx=20, pady=20)
canvas = Canvas(width=240, height=240, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(120, 120, image=logo)
canvas.grid(column=1, row=1)



window.mainloop()