print("Welcome to the Basic Quiz!")
print("1. Play Quiz")
print("2. Exit")
easy_questions = [
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["A) Ag", "B) Au", "C) Fe", "D) Pb"],
        "answer": "B" 
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Shark"],
        "answer": "B"
    }
]
medium_questions = [
    {
        "question": "What is the hottest planet in our solar system?",
        "options": ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"],
        "answer": "A"
    },
    {
        "question": "Which element has the highest boiling point?",
        "options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Oganesson"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Neptune"],
        "answer": "B"
    }
]
choice = input("Enter your choice 1 or 2:")
while choice not in ["1","2"]:
    print("Invalid choice. Please enter 1 or 2.")
    choice = input("Enter your choice 1 or 2:")
if choice == "1":
    lvl=input("Choose your level: Easy, Medium, Hard:")
    if lvl.lower() =="easy":
        score = 0
        for q in easy_questions:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = input("Enter your answer (A, B, C, D): ")
            if answer.upper() == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("incorrect. The correct answer is:", q["answer"])
                print("Your final score is:", score, "out of", len(easy_questions))
    if lvl.lower() == "medium":
        score = 0
        for q in medium_questions:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = input("Enter your answer (A, B. C, D): ")
            if answer.upper() == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("incorrect. The corrrect answer is:", q["answer"])
                print("Your final score is:", score, "out of", len(medium_questions))