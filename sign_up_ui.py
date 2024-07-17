import tkinter as tk
from tkinter import messagebox
import quiz_app_db
import functions as func

class SignUpUI:

    def __init__(self, root, login_callback):
        self.db = quiz_app_db.QuizAppDB()

        self.root = root
        self.root.title("Sign Up")

        self.login_callback = login_callback

        self.label_username = tk.Label(root, text="Username")
        self.label_username.grid(row=0, column=0, padx=10, pady=10)

        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(root, text="Password")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_password = tk.Entry(root, show='*')
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.button_signup = tk.Button(root, text="Sign Up", command=self.sign_up)
        self.button_signup.grid(row=2, columnspan=2, pady=10)

    def sign_up(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            self.db.add_user(username, password)
            messagebox.showinfo("Success", "Account created successfully!")

            # Debug statement to print the inserted user
            cursor = self.db.get_cursor
            cursor.execute('SELECT * FROM User')
            users = cursor.fetchall()
            print("Users in database after sign up:", users)

            self.root.destroy()
            self.login_callback()
        except Exception as e:
            messagebox.showerror("Error", str(e))
