import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
""")
conn.commit()

def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        listbox.insert(tk.END, row[1])

def add_task():
    task = entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    entry.delete(0, tk.END)
    load_tasks()

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        task_text = listbox.get(selected_index)

        cursor.execute("DELETE FROM tasks WHERE task = ?", (task_text,))
        conn.commit()
        load_tasks()
    except:
        messagebox.showwarning("Warning", "No task selected!")

def edit_task():
    try:
        selected_index = listbox.curselection()[0]
        old_task = listbox.get(selected_index)
        new_task = entry.get()

        if new_task.strip() == "":
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return

        cursor.execute("UPDATE tasks SET task = ? WHERE task = ?", (new_task, old_task))
        conn.commit()
        entry.delete(0, tk.END)
        load_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to edit!")

def select_task(event):
    try:
        selected_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_index)
        entry.delete(0, tk.END)
        entry.insert(0, selected_task)
    except:
        pass

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

edit_btn = tk.Button(btn_frame, text="Edit Task", width=12, command=edit_task)
edit_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)


listbox = tk.Listbox(root, width=45, height=15)
listbox.pack(pady=10)

listbox.bind("<<ListboxSelect>>", select_task)

load_tasks()

root.mainloop()

conn.close()