import tkinter as tk
from tkinter import messagebox
from quiz_app_db import QuizAppDB
import random


class QuizUI:

    def __init__(self, root, user_id):
        self.db = QuizAppDB()
        self.user_id = user_id

        self.root = root
        self.root.title("Select Category")

        self.label_category = tk.Label(root, text="Select Category")
        self.label_category.grid(row=0, column=0, padx=10, pady=10)

        self.category_var = tk.StringVar(root)
        self.category_var.set("GeneralKnowledge")
        self.categories = ["GeneralKnowledge", "Science", "Maths", "Literature", "Sports"]
        self.option_menu = tk.OptionMenu(root, self.category_var, *self.categories)
        self.option_menu.grid(row=0, column=1, padx=10, pady=10)

        self.button_start = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.button_start.grid(row=1, columnspan=2, pady=10)

    def start_quiz(self):
        category = self.category_var.get()
        self.questions = self.db.get_questions_by_category(category)
        if not self.questions:
            messagebox.showerror("Error", "No questions available for the selected category")
            return

        self.current_question = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question]

        # Shuffle the answer options
        options = [question[3], question[4], question[5], question[6]]
        correct_answer = question[7]
        random.shuffle(options)

        # Find the index of the correct answer after shuffling
        correct_index = options.index(correct_answer)

        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title("Quiz")

        self.label_question = tk.Label(self.quiz_window, text=question[2])
        self.label_question.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.answer_var = tk.StringVar()
        self.answer_var.set(None)

        self.radio_answer1 = tk.Radiobutton(self.quiz_window, text=options[0], variable=self.answer_var,
                                            value=options[0])
        self.radio_answer1.grid(row=1, column=0, padx=10, pady=5)
        self.radio_answer2 = tk.Radiobutton(self.quiz_window, text=options[1], variable=self.answer_var,
                                            value=options[1])
        self.radio_answer2.grid(row=1, column=1, padx=10, pady=5)
        self.radio_answer3 = tk.Radiobutton(self.quiz_window, text=options[2], variable=self.answer_var,
                                            value=options[2])
        self.radio_answer3.grid(row=2, column=0, padx=10, pady=5)
        self.radio_answer4 = tk.Radiobutton(self.quiz_window, text=options[3], variable=self.answer_var,
                                            value=options[3])
        self.radio_answer4.grid(row=2, column=1, padx=10, pady=5)

        self.button_next = tk.Button(self.quiz_window, text="Next", command=self.next_question)
        self.button_next.grid(row=3, columnspan=2, pady=10)

    def next_question(self):
        selected_answer = self.answer_var.get()
        correct_answer = self.questions[self.current_question][7]

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.quiz_window.destroy()
            self.show_question()
        else:
            self.quiz_window.destroy()
            self.show_results()

    def show_results(self):
        self.db.save_quiz_result(self.user_id, self.category_var.get(), self.score)
        messagebox.showinfo("Quiz Completed", f"You scored {self.score}/{len(self.questions)}")

