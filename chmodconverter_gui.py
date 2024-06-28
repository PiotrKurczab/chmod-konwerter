import tkinter as tk
from tkinter import messagebox
import chmodconverter_functions as chmodconverter

def update_numeric():
    symbolic = symbolic_entry.get()
    try:
        numeric = chmodconverter.symbolic_to_numeric(symbolic)
        numeric_entry.delete(0, tk.END)
        numeric_entry.insert(0, numeric)
        update_checkboxes(symbolic)
    except Exception as e:
        messagebox.showerror("Error", "Invalid symbolic permissions")

def update_symbolic():
    numeric = numeric_entry.get()
    try:
        symbolic = chmodconverter.numeric_to_symbolic(numeric)
        symbolic_entry.delete(0, tk.END)
        symbolic_entry.insert(0, symbolic)
        update_checkboxes(symbolic)
    except Exception as e:
        messagebox.showerror("Error", "Invalid numeric permissions")

def update_checkboxes(symbolic):
    permissions = [
        owner_read, owner_write, owner_execute,
        group_read, group_write, group_execute,
        other_read, other_write, other_execute
    ]
    for i, perm in enumerate(symbolic):
        permissions[i].var.set(perm != '-')

def update_from_checkboxes():
    symbolic = ''
    for i in range(0, 9, 3):
        group = ''
        group += 'r' if checkboxes[i].var.get() else '-'
        group += 'w' if checkboxes[i+1].var.get() else '-'
        group += 'x' if checkboxes[i+2].var.get() else '-'
        symbolic += group
    
    symbolic_entry.delete(0, tk.END)
    symbolic_entry.insert(0, symbolic)
    numeric = chmodconverter.symbolic_to_numeric(symbolic)
    numeric_entry.delete(0, tk.END)
    numeric_entry.insert(0, numeric)

# Create main application window
app = tk.Tk()
app.title("chmod Converter")
app.geometry("600x300")

# Configure styles
app.configure(bg="#F7F7F7")
font_large = ("Helvetica", 14, "bold")
font_medium = ("Helvetica", 12)
font_small = ("Helvetica", 10)

# Create main frame
main_frame = tk.Frame(app, bg="#F7F7F7")
main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Permissions label
tk.Label(main_frame, text="Permissions:", font=font_large, bg="#F7F7F7").grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Numeric entry
numeric_entry = tk.Entry(main_frame, font=font_medium, width=10)
numeric_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
numeric_entry.bind("<KeyRelease>", lambda event: update_symbolic())

# Symbolic entry
symbolic_entry = tk.Entry(main_frame, font=font_medium, width=20)
symbolic_entry.grid(row=0, column=2, padx=10, pady=10, sticky="w")
symbolic_entry.bind("<KeyRelease>", lambda event: update_numeric())

# Spacer
tk.Label(main_frame, text="", bg="#F7F7F7").grid(row=1, column=0, padx=0, pady=10)

# Column labels
tk.Label(main_frame, text="Owner", font=font_medium, bg="#F7F7F7").grid(row=2, column=1, padx=10, pady=10)
tk.Label(main_frame, text="Group", font=font_medium, bg="#F7F7F7").grid(row=2, column=2, padx=10, pady=10)
tk.Label(main_frame, text="Other", font=font_medium, bg="#F7F7F7").grid(row=2, column=3, padx=10, pady=10)

# Row labels
tk.Label(main_frame, text="Read", font=font_medium, bg="#F7F7F7").grid(row=3, column=0, padx=0, pady=10)
tk.Label(main_frame, text="Write", font=font_medium, bg="#F7F7F7").grid(row=4, column=0, padx=0, pady=10)
tk.Label(main_frame, text="Execute", font=font_medium, bg="#F7F7F7").grid(row=5, column=0, padx=0, pady=10)

def create_checkbox(row, column):
    cb = tk.Checkbutton(main_frame, bg="#F7F7F7", selectcolor="#FFFFFF")
    cb.var = tk.IntVar()
    cb.config(variable=cb.var, command=update_from_checkboxes)
    cb.grid(row=row, column=column, padx=10, pady=5)
    return cb

# Create checkboxes for owner, group, and other permissions
owner_read = create_checkbox(3, 1)
owner_write = create_checkbox(4, 1)
owner_execute = create_checkbox(5, 1)

group_read = create_checkbox(3, 2)
group_write = create_checkbox(4, 2)
group_execute = create_checkbox(5, 2)

other_read = create_checkbox(3, 3)
other_write = create_checkbox(4, 3)
other_execute = create_checkbox(5, 3)

checkboxes = [
    owner_read, owner_write, owner_execute,
    group_read, group_write, group_execute,
    other_read, other_write, other_execute
]

# Start the application
app.mainloop()