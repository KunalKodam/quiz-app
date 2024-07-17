# Quiz Application

This is a quiz application built with Python using the Tkinter library for the GUI and SQLite for the database. The application allows users to sign up, log in, select a quiz category, and take a quiz. The results of the quiz are saved, and users can see their scores at the end of the quiz.

## Features

- User Sign Up and Log In
- Quiz Categories: General Knowledge, Science, Maths, Literature, and Sports
- Randomized questions and shuffled answer options
- Scoring and result storage

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/KunalKodam/quiz-app.git
    cd quiz-app
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the application**:
    ```sh
    python main.py
    ```

## Project Structure

- `main.py`: Main script to start the application.
- `db_base.py`: Base class for database operations.
- `quiz_app_db.py`: Class for handling the quiz database.
- `functions.py`: Additional utility functions.
- `login_ui.py`: User Interface for login.
- `sign_up_ui.py`: User Interface for sign-up.
- `quiz_ui.py`: User Interface for the quiz.
- `questions.csv`: CSV file containing the quiz questions.

## Usage

1. **Sign Up**: Open the application and click on "Sign Up" to create a new user account.
2. **Log In**: Log in with your username and password.
3. **Select Category**: Choose a quiz category and start the quiz.
4. **Answer Questions**: Answer the questions by selecting the correct option.
5. **View Results**: At the end of the quiz, view your score.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes.




