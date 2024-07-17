import tkinter as tk
from tkinter import messagebox
import quiz_app_db
import functions as func


class LoginUI:

    def __init__(self, root, signup_callback, quiz_callback):
        self.db = quiz_app_db.QuizAppDB()

        self.root = root
        self.root.title("Login")

        self.signup_callback = signup_callback
        self.quiz_callback = quiz_callback

        self.label_username = tk.Label(root, text="Username")
        self.label_username.grid(row=0, column=0, padx=10, pady=10)

        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(root, text="Password")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_password = tk.Entry(root, show='*')
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.grid(row=2, columnspan=2, pady=10)

        self.button_signup = tk.Button(root, text="Sign Up", command=self.open_signup)
        self.button_signup.grid(row=3, columnspan=2, pady=10)

        self.button_delete = tk.Button(root, text="Delete Account", command=self.delete_account)
        self.button_delete.grid(row=4, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        cursor = self.db.get_cursor
        cursor.execute('SELECT user_id FROM User WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            self.quiz_callback(user[0])
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def delete_account(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            self.db.delete_user(username, password)
            messagebox.showinfo("Success", "Account deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error : Username and password do not match existing user", str(e))

    def open_signup(self):
        self.root.destroy()
        self.signup_callback()
