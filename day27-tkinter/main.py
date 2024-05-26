from tkinter import *
import turtle

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="bottom")  # pack(): place to the screen
# my_label.pack(expand=True)  # expand=True: place in the middle of the screen
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=100, pady=100)


# Button
def button_clicked():
   """ Show Button Got Clicked on my_label when the button get's clicked """
   # my_label.config(text="Button got clicked")
   new_text = input.get()
   my_label.config(text=new_text)
   print("I got clicked")

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
## grid and pack is incompatible, cannot use both at the same time ##

button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=4, row=3)
print(input.get())


# # Text
# text = Text(width=30, height=5)
# # Puts cursor in textbox
# text.focus()
# # Adds some text to begin with
# text.insert(END, "Example of multi-line text entry.")
# # Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()


# # Spinbox
# def spinbox_used():
#    # gets the current value in spinbox
#    print(spinbox.get())

# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()


# # Scale
# def scale_used(value):
#    print(value)

# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()


# # Checkbutton
# def checkbutton_used():
#    # Prints 1 if On button checked, otherwise 0
#    print(checked_state.get())

# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()


# # Radiobutton
# def radio_used():
#    print(radio_state.get())

# # variable to hold on to which radio button value is checked
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# # Listbox
# def listbox_used(event):
#    # gets current selection from listbox
#    print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#    listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# tim = turtle.Turtle()
# tim.write("Some text")

window.mainloop()
