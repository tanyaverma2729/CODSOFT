import tkinter

root = tkinter.Tk()
root.title("Calculator")

expression = ""

def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
    
def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)
            
label_result = tkinter.Label(root, text="")
label_result.grid(row=0, column=0, columnspan=4)

button_1 = tkinter.Button(root, text="1",background="red", command=lambda: add("1"), height=1, width=7)
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="2",background="silver", command=lambda: add("2"), height=1, width=7)
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="3",background="red", command=lambda: add("3"), height=1, width=7)
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text="/",background="silver", command=lambda: add("/"), height=1, width=7)
button_divide.grid(row=1, column=3)

button_4 = tkinter.Button(root, text="4",background="red", command=lambda: add("4"), height=1, width=7)
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, text="5",background="silver", command=lambda: add("5"), height=1, width=7)
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text="6",background="red", command=lambda: add("6"), height=1, width=7)
button_6.grid(row=2, column=2)

button_multiply = tkinter.Button(root, text="*",background="silver", command=lambda: add("*"), height=1, width=7)
button_multiply.grid(row=2, column=3)

button_7 = tkinter.Button(root, text="7",background="red", command=lambda: add("7"), height=1, width=7)
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, text="8",background="silver", command=lambda: add("8"), height=1, width=7)
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(root, text="9",background="red", command=lambda: add("9"), height=1, width=7)
button_9.grid(row=3, column=2)

button_subtract = tkinter.Button(root, text="-",background="silver", command=lambda: add("-"), height=1, width=7)
button_subtract.grid(row=3, column=3)

button_clear = tkinter.Button(root, text="C",background="red", command=lambda: clear(), height=1, width=7)
button_clear.grid(row=4, column=0)

button_0 = tkinter.Button(root, text="0",background="silver", command=lambda: add("0"), height=1, width=7)
button_0.grid(row=4, column=1)

button_dot = tkinter.Button(root, text=".",background="red", command=lambda: add("."), height=1, width=7)
button_dot.grid(row=4, column=2)

button_add = tkinter.Button(root, text="+",background="silver", command=lambda: add("+"), height=1, width=7)
button_add.grid(row=4, column=3)


button_equals = tkinter.Button(root, text="=", background="silver", width=16, command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=4)


root.mainloop()