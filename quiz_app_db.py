import os
import sqlite3
import db_base as db
import csv

class QuizAppDB(db.DBbase):

    def __init__(self):
        super().__init__("quizappdb.sqlite")
        if not os.path.exists("quizappdb.sqlite"):
            self.reset_database()
            self.load_questions_from_csv("questions.csv")  # Load questions when the database is created

    def reset_database(self):
        sql = """
            DROP TABLE IF EXISTS User;
            DROP TABLE IF EXISTS Questions;
            DROP TABLE IF EXISTS QuizResults;

            CREATE TABLE User (
                user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                username TEXT UNIQUE,
                password TEXT
            );

            CREATE TABLE Questions (
                question_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                category TEXT,
                question TEXT,
                answer1 TEXT,
                answer2 TEXT,
                answer3 TEXT,
                answer4 TEXT,
                correct_answer TEXT
            );

            CREATE TABLE QuizResults (
                result_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                user_id INTEGER,
                category TEXT,
                score INTEGER,
                FOREIGN KEY(user_id) REFERENCES User(user_id)
            ); """
        super().execute_script(sql)

    def add_user(self, username, password):
        cursor = super().get_cursor
        cursor.execute('INSERT INTO User (username, password) VALUES (?, ?)', (username, password))
        super().get_connection.commit()

    def delete_user(self, username, password):
        cursor = super().get_cursor
        cursor.execute('DELETE FROM User WHERE username = ? AND password = ?', (username, password))
        super().get_connection.commit()

    def load_questions_from_csv(self, csv_filename):
        with open(csv_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    self.add_question(
                        row['Category'],
                        row['Question'],
                        row['Answer Option 1'],
                        row['Answer Option 2'],
                        row['Answer Option 3'],
                        row['Answer Option 4'],
                        row['Correct Answer']
                    )
                except ValueError as e:
                    print(f"Error processing row: {row}")
                    print(f"ValueError: {e}")

    def add_question(self, category, question, answer1, answer2, answer3, answer4, correct_answer):
        cursor = super().get_cursor
        cursor.execute('''INSERT INTO Questions (category, question, answer1, answer2, answer3, answer4, correct_answer)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                          (category, question, answer1, answer2, answer3, answer4, correct_answer))
        super().get_connection.commit()

    def get_questions_by_category(self, category, limit=5):
        cursor = super().get_cursor
        cursor.execute('''SELECT * FROM Questions WHERE category = ? ORDER BY RANDOM() LIMIT ?''', (category, limit))
        return cursor.fetchall()

    def save_quiz_result(self, user_id, category, score):
        cursor = super().get_cursor
        cursor.execute('''INSERT INTO QuizResults (user_id, category, score)
                          VALUES (?, ?, ?)''', (user_id, category, score))
        super().get_connection.commit()

# Testing the loading of questions from CSV
# quiz_app_kunal = QuizAppDB()
# quiz_app_kunal.reset_database()
# quiz_app_kunal.load_questions_from_csv("questions.csv")
# quiz_app_kunal.close_db()
# print("Questions loaded successfully")


