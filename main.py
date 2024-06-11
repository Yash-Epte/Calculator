import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_results.insert(tk.END, symbol)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_results.delete(1.0, tk.END)
        text_results.insert(1.0, result)
    except:
        clear_field()
        text_results.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_results.delete(1.0, tk.END)
    text_results.insert(1.0, "0")

root = tk.Tk()
root.title("Calculator")
root.geometry("290x270")
root.resizable(0, 0)

# Create a frame for the text field
text_frame = tk.Frame(root)
text_frame.pack(pady=10)

# Create the text field
text_results = tk.Text(text_frame, height=2, width=16, font=('Arial', 24))
text_results.pack()


# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Numeric and addition buttons
btn1 = tk.Button(button_frame, text="1", command=lambda: add_to_calculation(1), width=5, font=('Arial', 14), bg="gray", fg="white")
btn1.grid(row=2, column=0)

btn2 = tk.Button(button_frame, text="2", command=lambda: add_to_calculation(2), width=5, font=('Arial', 14), bg="gray", fg="white")
btn2.grid(row=2, column=1)

btn3 = tk.Button(button_frame, text="3", command=lambda: add_to_calculation(3), width=5, font=('Arial', 14), bg="gray", fg="white")
btn3.grid(row=2, column=2)

btn_add = tk.Button(button_frame, text="+", command=lambda: add_to_calculation("+"), width=5, font=('Arial', 14), bg="gray", fg="white")
btn_add.grid(row=2, column=3)

# Numeric and subtraction buttons
btn4 = tk.Button(button_frame, text="4", command=lambda: add_to_calculation(4), width=5, font=('Arial', 14), bg="gray", fg="white")
btn4.grid(row=3, column=0)

btn5 = tk.Button(button_frame, text="5", command=lambda: add_to_calculation(5), width=5, font=('Arial', 14), bg="gray", fg="white")
btn5.grid(row=3, column=1)

btn6 = tk.Button(button_frame, text="6", command=lambda: add_to_calculation(6), width=5, font=('Arial', 14), bg="gray", fg="white")
btn6.grid(row=3, column=2)

btn_sub = tk.Button(button_frame, text="-", command=lambda: add_to_calculation("-"), width=5, font=('Arial', 14), bg="gray", fg="white")
btn_sub.grid(row=3, column=3)

# Numeric and multiplication buttons
btn7 = tk.Button(button_frame, text="7", command=lambda: add_to_calculation(7), width=5, font=('Arial', 14), bg="gray", fg="white")
btn7.grid(row=4, column=0)

btn8 = tk.Button(button_frame, text="8", command=lambda: add_to_calculation(8), width=5, font=('Arial', 14), bg="gray", fg="white")
btn8.grid(row=4, column=1)

btn9 = tk.Button(button_frame, text="9", command=lambda: add_to_calculation(9), width=5, font=('Arial', 14), bg="gray", fg="white")
btn9.grid(row=4, column=2)

btn_mul = tk.Button(button_frame, text="x", command=lambda: add_to_calculation("*"), width=5, font=('Arial', 14), bg="gray", fg="white")
btn_mul.grid(row=4, column=3)

# Brackets and 0 buttons, division buttons
btn_open = tk.Button(button_frame, text="(", command=lambda: add_to_calculation("("), width=5, font=('Arial', 14), bg="gray", fg="white")
btn_open.grid(row=5, column=0)

btn0 = tk.Button(button_frame, text="0", command=lambda: add_to_calculation(0), width=5, font=('Arial', 14), bg="gray", fg="white")
btn0.grid(row=5, column=1)

btn_close = tk.Button(button_frame, text=")", command=lambda: add_to_calculation(")"), width=5, font=('Arial', 14), bg="gray", fg="white")
btn_close.grid(row=5, column=2)

btn_div = tk.Button(button_frame, text="/", command=lambda: add_to_calculation("/"), width=5, font=('Arial', 14), bg="gray", fg="white")
btn_div.grid(row=5, column=3)

# Clear and Equal buttons
btn_clear = tk.Button(button_frame, text="C", command=lambda: clear_field(), width=14, font=('Arial', 14), bg="red", fg="white")
btn_clear.grid(row=6, column=0, columnspan=2)

btn_equal = tk.Button(button_frame, text="=", command=lambda: evaluate_calculation(), width=14, font=('Arial', 14), bg="green", fg="white")
btn_equal.grid(row=6, column=2, columnspan=2)

# Keep the window open
root.mainloop()