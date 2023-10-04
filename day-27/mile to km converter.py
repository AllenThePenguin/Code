from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=60)
window.config(padx=20, pady=20)


def calculate(miles):
    output = round(float(miles)*1.60934, 2)
    return output


def click_button():
    result = calculate(miles_num.get())
    km_num.config(text=result)


miles_num = Entry(width=5)
miles_num.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

km_num = Label(text="0")
km_num.grid(row=1, column=1)

label3 = Label(text="Km")
label3.grid(row=1, column=2)

button = Button(text="Calculate", command=click_button)
button.grid(row=2, column=1)
window.mainloop()
