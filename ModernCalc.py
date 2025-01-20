import tkinter
from tkinter import END
from tkinter import messagebox
window = tkinter.Tk()

window.title("Modern Calculator App")

#setting the window size
window.geometry("420x420")

# setting the background color. There is a method called config that we will use.
window.config(bg="black")

# creating the entry field where the number that is typed will be displayed
entryfield = tkinter.Entry(window,font=("Arial", 20, "bold"))
entryfield.grid(row=0, column = 0, columnspan = 4, pady = 10, padx = 10)

# defining function for functionality

# creating a function for the delete button
def clear():
    entryfield.delete(0, END)

#ONCE THE NUMBERS/DIGITS ARE PRESSED, WE WANT THEM TO BE INSERTED INTO THE ENTRY FIELD.
def click(number):
    entryfield.insert(END, number)

# we are creating a function for the equal sign
def answer():
    expression = entryfield.get()
    try:
        result = eval(expression)
        ans = round(result, 1)
        entryfield.delete(0, END)
        entryfield.insert(0, ans)
    except SyntaxError:
        messagebox.showerror("error", " Invalid expression")

    except ZeroDivisionError:
        messagebox.showerror("Invalid option, a number cannot be divided by zero")


#Creating all the GUI parts with numbers
btn7 = tkinter.Button(window, text="7", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (7))
btn7.grid(row=1, column=0, pady = 10, padx = 10)
btn8 = tkinter.Button(window, text="8", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (8))
btn8.grid(row=1, column=1)
btn9 = tkinter.Button(window, text="9", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (9))
btn9.grid(row=1, column=2)
btnadd = tkinter.Button(window, text="+", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click ("+"))
btnadd.grid(row=1, column=3)

btn4 = tkinter.Button(window, text="4", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (4))
btn4.grid(row=2, column=0, pady = 10, padx = 10)
btn5 = tkinter.Button(window, text="5", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (5))
btn5.grid(row=2, column=1)
btn6 = tkinter.Button(window, text="6", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (6))
btn6.grid(row=2, column=2)
btnminus = tkinter.Button(window, text="-", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click ("-"))
btnminus.grid(row=2, column=3)

btn1 = tkinter.Button(window, text="1", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (1))
btn1.grid(row=3, column=0, pady = 10, padx = 10)
btn2 = tkinter.Button(window, text="2", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (2))
btn2.grid(row=3, column=1)
btn3 = tkinter.Button(window, text="3", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (3))
btn3.grid(row=3, column=2)
btnmultiply = tkinter.Button(window, text="x", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click ("*"))
btnmultiply.grid(row=3, column=3)

btn_clear = tkinter.Button(window, text="C", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=clear)
btn_clear.grid(row=4, column=0, pady = 10, padx = 10)
btn_zero = tkinter.Button(window, text="0", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click (0))
btn_zero.grid(row=4, column=1)
btn_equals = tkinter.Button(window, text="=", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=answer)
btn_equals.grid(row=4, column=2, pady = 10, padx = 10)
btn_divide = tkinter.Button(window, text="/", font=("Arial", 20, 'bold'), width=5,  cursor = "hand2", command=lambda : click ("/"))
btn_divide.grid(row=4, column=3)


window.mainloop()

