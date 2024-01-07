from tkinter import *


def button_clicked():
    print("I got clicked")
    miles_val = int(miles_input.get())
    km_result.config(text=str(round(miles_val * 1.6)))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

#Label
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=50, pady=50)

#Label
equals = Label(text="is equal to", font=("Arial", 24, "bold"))
equals.grid(column=0, row=1)
equals.config(padx=50, pady=50)


km_result = Label(text="_", font=("Arial", 24, "bold"))
km_result.grid(column=1, row=1)
km_result.config(padx=50, pady=50)

#Label
km_val = Label(text="Km", font=("Arial", 24, "bold"))
km_val.grid(column=2, row=1)
km_val.config(padx=50, pady=50)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)









window.mainloop()