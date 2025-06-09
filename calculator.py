import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression():
    try:
        # Get the expression from the entry widget
        expression = entry.get()
        # Evaluate the expression and update the result label
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        # Show an error message if the evaluation fails
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to handle button click events
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget for the expression
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('.', 4, 2),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0), ('=', 4, 4)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, command=clear_entry)
    else:
        button = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
