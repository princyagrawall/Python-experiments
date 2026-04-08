import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib


conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def signup():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    hashed = hash_password(password)

    try:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hashed))
        conn.commit()
        messagebox.showinfo("Success", "Account created successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")


def login():
    username = entry_user.get()
    password = entry_pass.get()

    hashed = hash_password(password)

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials!")


root = tk.Tk()
root.title("Login & Signup System")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Signup", command=signup).pack(pady=5)
tk.Button(root, text="Login", command=login).pack(pady=5)

root.mainloop()