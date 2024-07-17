import tkinter as tk
from sign_up_ui import SignUpUI
from login_ui import LoginUI
from quiz_ui import QuizUI
from quiz_app_db import QuizAppDB

def show_signup_screen():
    root = tk.Tk()
    app = SignUpUI(root, show_login_screen)
    root.mainloop()

def show_login_screen():
    root = tk.Tk()
    app = LoginUI(root, show_signup_screen, start_quiz)
    root.mainloop()

def start_quiz(user_id):
    root = tk.Tk()
    app = QuizUI(root, user_id)
    root.mainloop()

if __name__ == "__main__":
    db = QuizAppDB()  # Initialize the database and load questions if needed
    show_login_screen()
