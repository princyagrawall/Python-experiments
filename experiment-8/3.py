import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT,
    phone TEXT
)
""")
conn.commit()


def add_student():
    name = name_entry.get()
    email = email_entry.get()
    course = course_entry.get()
    phone = phone_entry.get()

    if name == "" or email == "" or course == "" or phone == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    cursor.execute("INSERT INTO students (name, email, course, phone) VALUES (?, ?, ?, ?)",
                   (name, email, course, phone))
    conn.commit()

    messagebox.showinfo("Success", "Student Registered Successfully!")
    clear_fields()
    display_students()

def display_students():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(tk.END, row)

def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No student selected!")
        return

    student = listbox.get(selected[0])
    cursor.execute("DELETE FROM students WHERE id=?", (student[0],))
    conn.commit()

    messagebox.showinfo("Deleted", "Student deleted successfully!")
    display_students()

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Student Registration System")
root.geometry("500x500")


tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()


tk.Button(root, text="Register", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=display_students).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_student).pack(pady=5)


listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)


root.mainloop()