def run_quiz():
    questions = [
        {
            "question": "What is the keyword to define a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. define"],
            "answer": "B"
        },
        {
            "question": "Which movie features the quote 'I'll be back'?",
            "options": ["A. Terminator", "B. Rocky", "C. Rambo", "D. Matrix"],
            "answer": "A"
        },
        {
            "question": "What data type is used to store text in Python?",
            "options": ["A. int", "B. str", "C. bool", "D. float"],
            "answer": "B"
        },
        {
            "question": "Which character is the main wizard in the Harry Potter series?",
            "options": ["A. Frodo", "B. Dumbledore", "C. Harry", "D. Gandalf"],
            "answer": "C"
        }
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🏁 Quiz Over! You scored {score} out of {len(questions)}.")

# Game loop
while True:
    run_quiz()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("👋 Thanks for playing! Goodbye!")
        break
