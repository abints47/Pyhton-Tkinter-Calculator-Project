import tkinter as tk

app = tk.Tk()
app.geometry("400x600")
app.title("Calculator")
app.configure(background="#1B2342")

# 1. The Display Screen
# columnspan=4 allows it to span the full width of the calculator grid
display = tk.Entry(app, font=("Arial", 24), borderwidth=5, relief="flat", justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 50), sticky="nsew")

# 2. Define Button Labels in a Grid Layout (Rows and Columns)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
]


def btn_click(number):
    # Get what is currently in the display
    current = display.get()
    # Delete the old content
    display.delete(0, tk.END)
    # Put the old content + the new number back in
    display.insert(0, str(current) + str(number))



def btn_clear():
    """Removes all text from the display screen."""
    display.delete(0, tk.END)


def btn_equal():
    """Calculates the result and prints it to the display."""
    try:
        # Get the math expression from display (e.g., "5+5")
        expression = display.get()
        # Replace the 'x' with '*' for Python to understand multiplication
        expression = expression.replace('x', '*')

        # eval() processes the string as a math equation
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, result)
        print(f"Calculation Result: {result}")  # Prints to your PyCharm console
    except Exception:
        # If the user types something invalid like "++5"
        display.delete(0, tk.END)
        display.insert(0, "Error")

# 3. Create and Place Buttons using a Loop
# This replaces 32 lines of repetitive code with just 5 lines
# 3. Create and Place Buttons using a Loop
# 3. Create and Place Buttons using a Loop
for (text, r, c) in buttons:
    if text == 'C':
        cmd = btn_clear
    elif text == '=':
        cmd = btn_equal
    else:
        cmd = lambda t=text: btn_click(t)

    btn = tk.Button(app, text=text, fg="white", bg="#1F6AA4",
                    width=7, height=3, font=("Arial", 12, "bold"),
                    relief="flat", borderwidth=0, command=cmd)

    btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")













app.mainloop()