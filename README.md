# Basic Python Quiz

My first terminal-based quiz game, built while learning Python fundamentals. It lets you choose a difficulty level, answer multiple-choice questions, track your score, and replay the quiz as many times as you want during the session.

## What it does

* Provides a simple terminal-based quiz with Easy, Medium, and Hard difficulty levels
* Contains different questions and answers for each difficulty level
* Gives you multiple attempts to answer each question
* Shows whether your answer is correct or wrong
* Displays the correct answer when you run out of attempts
* Keeps track of your score throughout the quiz
* Shows your final score after completing the selected difficulty level
* Allows you to replay the quiz multiple times
* Returns to the main menu after each completed quiz
* Lets you exit the program whenever you choose
* Validates menu and difficulty-level input so invalid choices don't continue

## How to run it

```bash
python quiz_game.py
```

You'll see a menu:

```text
=== BASIC QUIZ ===
1. Play Quiz
2. Exit
```

* **1** — start the quiz and choose a difficulty level
* **2** — exit the program

After choosing to play, you'll be asked:

```text
Choose your level (Easy, Medium, Hard):
```

You can choose:

* **Easy** — 3 questions with up to 5 attempts per question
* **Medium** — 3 questions with up to 3 attempts per question
* **Hard** — 3 questions with up to 3 attempts per question

For each question, choose an answer using `A`, `B`, `C`, or `D`.

Example:

```text
What is the chemical symbol for Gold?
A) Ag
B) Au
C) Fe
D) Pb

Enter your answer (A, B, C, D): B
Correct!
```

At the end of the quiz, your final score is displayed:

```text
Your final score is: 3 out of 3
```

After completing the quiz, the main menu appears again, allowing you to play another quiz or exit.

## What I learned building this

* Storing quiz questions, options, and answers using lists and dictionaries
* Using `if`, `elif`, and `else` to handle different choices and difficulty levels
* Using `for` loops to go through multiple questions and answer options
* Using `while` loops to control attempts and keep the quiz running
* Using `while True` with `break` to allow the user to replay the quiz until they choose to exit
* Using `.lower()` and `.upper()` to make user input case-insensitive
* Tracking the player's score with a variable
* Using `len()` to calculate the total number of questions
* Giving users multiple attempts instead of ending the quiz after one wrong answer
* Validating user input and displaying helpful error messages
* Practicing nested loops and conditional logic in a real-world project
