def ask_question(question, answer):
    user_input = input(question + "\n> ").strip().lower()
    return user_input == answer.lower()

score = 0

print("Welcome to the Quiz!")

if ask_question("What is the capital of India?", "New Delhi"):
    score += 1
if ask_question("What does CPU stand for?", "Central Processing Unit"):
    score += 1
if ask_question("Who developed Python?", "Guido van Rossum"):
    score += 1

print(f"\nYou got {score}/3 correct!")
