from tkinter import *
# Importing all classes and functions from the tkinter module.

screen = Tk()
# Create an instance of the Tk class, representing the main window or root window.

screen.title("CALCULATOR")
# Set the title of the window to "CALCULATOR".

screen.geometry('365x490')
# Set the dimensions of the window to 365x490 pixels.

def click(number):
    global operator
    operator += str(number)
    text.set(operator)
    # Event handler function for button clicks. Appends the clicked number or operator to the global operator variable, updates the text variable, and displays it in the entry widget.

def clear():
    global operator
    operator = ''
    text.set(operator)
    # Event handler function to clear the calculator. Resets the global operator variable and updates the text variable to an empty string.

text = StringVar()
operator = ''
entry = Entry(screen, bg='pink', font=('timesroman', 20), bd='30', justify='right', textvariable=text)
# Create an Entry widget with custom background color, font, border width, and text justification.

entry.grid(row=0, columnspan=4)
# Place the Entry widget at row 0, spanning 4 columns on a grid layout.

btn7 = Button(screen, text='7', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(7))
# Create a Button widget with the label '7' and associate the click event handler with the lambda function.

btn7.grid(row=1, column=0)
# Place the Button widget at row 1, column 0 on a grid layout.

btn8 = Button(screen, text='8', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(8))
# Create a Button widget with the label '8' and associate the click event handler with the lambda function.

btn8.grid(row=1, column=1)
# Place the Button widget at row 1, column 1 on a grid layout.

btn9 = Button(screen, text='9', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(9))
# Create a Button widget with the label '9' and associate the click event handler with the lambda function.

btn9.grid(row=1, column=2)
# Place the Button widget at row 1, column 2 on a grid layout.

btnadd = Button(screen, text='+', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click('+'))
# Create a Button widget with the label '+' and associate the click event handler with the lambda function.

btnadd.grid(row=1, column=3)
# Place the Button widget at row 1, column 3 on a grid layout.

btn4 = Button(screen, text='4', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(4))
# Create a Button widget with the label '4' and associate the click event handler with the lambda function.

btn4.grid(row=2, column=0)
# Place the Button widget at row 2, column 0 on a grid layout.

btn5 = Button(screen, text='5', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(5))
# Create a Button widget with the label '5' and associate the click event handler with the lambda function.

btn5.grid(row=2, column=1)
# Place the Button widget at row 2, column 1 on a grid layout.

btn6 = Button(screen, text='6', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(6))
# Create a Button widget with the label '6' and associate the click event handler with the lambda function.

btn6.grid(row=2, column=2)
# Place the Button widget at row 2, column 2 on a grid layout.

btnsubstraction = Button(screen, text='-', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click('-'))
# Create a Button widget with the label '-' and associate the click event handler with the lambda function.

btnsubstraction.grid(row=2, column=3)
# Place the Button widget at row 2, column 3 on a grid layout.

btn3 = Button(screen, text='3', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(3))
# Create a Button widget with the label '3' and associate the click event handler with the lambda function.

btn3.grid(row=3, column=0)
# Place the Button widget at row 3, column 0 on a grid layout.

btn2 = Button(screen, text='2', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(2))
# Create a Button widget with the label '2' and associate the click event handler with the lambda function.

btn2.grid(row=3, column=1)
# Place the Button widget at row 3, column 1 on a grid layout.

btn1 = Button(screen, text='1', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(1))
# Create a Button widget with the label '1' and associate the click event handler with the lambda function.

btn1.grid(row=3, column=2)
# Place the Button widget at row 3, column 2 on a grid layout.

btnmulti = Button(screen, text='*', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click('*'))
# Create a Button widget with the label '*' and associate the click event handler with the lambda function.

btnmulti.grid(row=3, column=3)
# Place the Button widget at row 3, column 3 on a grid layout.

btn0 = Button(screen, text='0', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click(0))
# Create a Button widget with the label '0' and associate the click event handler with the lambda function.

btn0.grid(row=4, column=0)
# Place the Button widget at row 4, column 0 on a grid layout.

btnclear = Button(screen, text='C', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=clear)
# Create a Button widget with the label 'C' and associate the clear event handler.

btnclear.grid(row=4, column=1)
# Place the Button widget at row 4, column 1 on a grid layout.

btnequal = Button(screen, text='=', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click('='))
# Create a Button widget with the label '=' and associate the click event handler with the lambda function.

btnequal.grid(row=4, column=3)
# Place the Button widget at row 4, column 3 on a grid layout.

btndiv = Button(screen, text='/', font=('timesroman', 10, 'bold'), bd='8', padx=16, pady=16, command=lambda: click('/'))
# Create a Button widget with the label '/' and associate the click event handler with the lambda function.

btndiv.grid(row=4, column=2)
# Place the Button widget at row 4, column 2 on a grid layout.

screen.mainloop()
# Start the event loop to run the GUI application. It listens for events and triggers the associated event handlers or callbacks. The window remains visible and responsive until closed by the user.
