import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to remove the selected task from the list
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

# Function to mark the selected task as completed
def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, f"{task} - Completed")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create the entry widget for entering tasks
task_entry = tk.Entry(root, width=50, borderwidth=5)
task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Create the buttons
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.grid(row=1, column=0, padx=5, pady=5)

remove_button = tk.Button(root, text="Remove Task", width=15, command=remove_task)
remove_button.grid(row=1, column=1, padx=5, pady=5)

complete_button = tk.Button(root, text="Mark Completed", width=15, command=mark_completed)
complete_button.grid(row=1, column=2, padx=5, pady=5)

# Create the listbox to display tasks
listbox = tk.Listbox(root, width=60, height=15, selectmode=tk.SINGLE, borderwidth=5, relief=tk.SUNKEN)
listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
