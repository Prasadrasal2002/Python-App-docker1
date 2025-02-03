import tkinter as tk
from tkinter import messagebox
from task_manager_db import create_table, add_task, fetch_tasks, mark_completed

# Create the main window
root = tk.Tk()
root.title('Task Manager')

# Create the table if not exists
create_table()

# Function to add a task
def add_task_gui():
    title = title_entry.get()
    description = description_entry.get()
    deadline = deadline_entry.get()

    if title and deadline:
        add_task(title, description, deadline)
        title_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
        display_tasks()
    else:
        messagebox.showerror("Input Error", "Title and Deadline are required.")

# Function to mark a task as complete
def complete_task(task_id):
    mark_completed(task_id)
    display_tasks()

# Function to display tasks
def display_tasks():
    tasks_listbox.delete(0, tk.END)
    tasks = fetch_tasks()
    for task in tasks:
        status = "Completed" if task[4] == 1 else "Pending"
        task_display = f"{task[0]} - {task[1]} (Deadline: {task[3]}) - {status}"
        tasks_listbox.insert(tk.END, task_display)

# GUI layout
tk.Label(root, text='Task Title').grid(row=0, column=0)
tk.Label(root, text='Description').grid(row=1, column=0)
tk.Label(root, text='Deadline').grid(row=2, column=0)

title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)
description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1)
deadline_entry = tk.Entry(root)
deadline_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Add Task", command=add_task_gui)
add_button.grid(row=3, column=0, columnspan=2)

tasks_listbox = tk.Listbox(root, width=50)
tasks_listbox.grid(row=4, column=0, columnspan=2)
tasks_listbox.bind('<Double-1>', lambda event: complete_task(int(tasks_listbox.get(tasks_listbox.curselection()[0]).split(' ')[0])))

# Initially display tasks
display_tasks()

root.mainloop()
