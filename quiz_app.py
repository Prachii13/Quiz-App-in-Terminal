quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) Berlin", "C) Madrid", "D) Rome"],
        "answer": "A"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Dickens", "B) Shakespeare", "C) Tolkien", "D) Austen"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Saturn", "C) Mars", "D) Mercury"],
        "answer": "C"
    },
    {
        "question": "What is 5 * 6?",
        "options": ["A) 11", "B) 20", "C) 30", "D) 36"],
        "answer": "C"
    }
]

def run_quiz():
    print("🧠 Welcome to the Quiz!")
    score = 0

    for index, q in enumerate(quiz_data):
        print(f"\nQ{index + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🎯 Your Final Score: {score}/{len(quiz_data)}")

if __name__ == "__main__":
    run_quiz()
