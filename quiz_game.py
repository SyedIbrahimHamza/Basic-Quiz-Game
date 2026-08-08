while True:
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

    hard_questions = [
        {
            "question": "What is the time complexity of binary search?",
            "options": ["A) O(n)", "B) O(log n)", "C) O(n²)", "D) O(1)"],
            "answer": "B"
        },
        {
            "question": "Which sorting algorithm is fastest on average?",
            "options": ["A) Bubble Sort", "B) Quick Sort", "C) Insertion Sort", "D) Selection Sort"],
            "answer": "B"
        },
        {

            "question": "What does __init__ represent in Python OOP?",
            "options": ["A) Destructor", "B) Constructor", "C) Method", "D) Variable"],
            "answer": "B"
    }
    ]

    choice = input("Enter your choice 1 or 2: ")
    while choice not in ["1", "2"]:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice 1 or 2: ")

    if choice == "1":
        lvl = input("Choose your level (Easy, Medium, Hard): ")
        while lvl.lower() not in ["easy", "medium", "hard"]:
            print("Invalid level! Please choose Easy, Medium, or Hard.")
            lvl = input("Choose your level again: ")
    
        score = 0
    
        if lvl.lower() == "easy":
            for q in easy_questions:
                print("\n" + q["question"])
                for option in q["options"]:
                    print(option)
            
                attempts = 5
                while attempts > 0:
                    answer = input("Enter your answer (A, B, C, D): ").upper()
                    if answer == q["answer"]:
                        print("Correct!")
                        score += 1
                        break
                    else:
                        attempts -= 1
                        if attempts > 0:
                            print(f"Wrong! {attempts} attempts left.")
                        else:
                            print(f"Wrong! Correct answer: {q['answer']}")
        
            print("\nYour final score is:", score, "out of", len(easy_questions))
    
        elif lvl.lower() == "medium":
            for q in medium_questions:
                print("\n" + q["question"])
                for option in q["options"]:
                    print(option)
            
                attempts = 3
                while attempts > 0:
                    answer = input("Enter your answer (A, B, C, D): ").upper()
                    if answer == q["answer"]:
                        print("Correct!")
                        score += 1
                        break
                    else:
                        attempts -= 1
                        if attempts > 0:
                            print(f"Wrong! {attempts} attempts left.")
                        else:
                            print(f"Wrong! Correct answer: {q['answer']}")
        
            print("\nYour final score is:", score, "out of", len(medium_questions))
    
        elif lvl.lower() == "hard":
            for q in hard_questions:
                print("\n" + q["question"])
                for option in q["options"]:
                    print(option)
            
                attempts = 3
                while attempts > 0:
                    answer = input("Enter your answer (A, B, C, D): ").upper()
                    if answer == q["answer"]:
                        print("Correct!")
                        score += 1
                        break
                    else:
                        attempts -= 1
                        if attempts > 0:
                            print(f"Wrong! {attempts} attempts left.")
                        else:
                            print(f"Wrong! Correct answer: {q['answer']}")
        
            print("\nYour final score is:", score, "out of", len(hard_questions))

    elif choice == "2":
        print("Goodbye! Thanks for playing!")
        break