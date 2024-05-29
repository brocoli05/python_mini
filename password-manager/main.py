from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    passwords = [website, email, password]
    # Write to the data inside the entries to a data.txt file when the Add button is clicked
    # Each website, email, and password combination should be on a new line inside the file
    # All fields need to be cleared after Add button is pressed
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        # data_file.writelines("%s | " % data for data in passwords)

    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")  # sticky: for alignment
website_input.focus()  # put cursor right after launching the app
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "abc@email.com")  # pre-entered value, END: cursor starts after the value
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
