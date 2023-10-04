from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.place(x=0, y=0)
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)


# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

button2 = Button(text="I'm also a Button")
button2.grid(row=0, column=2)


# Entry
input = Entry(width=10)
print(input.get())
input.grid(row=2, column=3)


window.mainloop()
