import random

questions = [
    { "question" : "What is the capital of Australia ?",
     "options": ["Sydney", "Canberra", "Melbourne", "Perth"],
     "answer" : "Canberra"},
    {"question" : "Which river is the longest in the world ?",
     "options": ["Mississippi", "Nile", "Amazon", "Ganga"],
     "answer" : "Nile"},
    {"question" : "What is the national currency of Japan ?",
     "options": ["Dollar", "Youn", "Ruppee", "Yen"],
     "answer" : "Yen"},
    {"question" : "Which planet is known as the Red Planet ?",
     "options": ["Mars", "Earth", "Mercury", "jupiter"],
     "answer" : "Mars"},
    {"question" : "Which key is used to refresh a webpage ?",
     "options": ["F4", "F2", "F5", "F6"],
     "answer" : "F5"},
    {"question" : "Who was the first President of India ?",
     "options": ["Jawahar Lal Nehru", "Subhashchandra Bose", "Rajendra Prasad", "Indira Gandhi"],
     "answer" : "Rajendra Prasad"},
    {"question" : "Which data structure uses FIFO principle ?",
     "options": ["Queue", "Stack", "Graph", "Tree"],
     "answer" : "Queue"},
    {"question" : "Which country gifted the Statue of Liberty to USA ?",
     "options": ["India", "Germany", "France", "Canada"],
     "answer" : "France"},
    {"question" : "What does IP stand for ?",
     "options": ["Internet Pointer", "Internet Procedure", "Internet Protocol", "Internal Protocol"],
     "answer" : "Internet Protocol"},
    {"question" : "What is the default port number of HTTPS ?",
     "options": ["441", "80", "88", "443"],
     "answer" : "443"}
]

def quiz():
    random.shuffle(questions)
    score = 0
    for que in questions:
        print("\n",que["question"])
        for index, option in enumerate(que["options"], start=1):
            print(f"{index}. {option}")
        user_ans = int(input("Your answer : "))
        correct_ans = que["answer"]
        if user_ans < 1 or user_ans > len(que["options"]):
            print("Invalid Choice !")
            continue
        if que["options"][user_ans-1].lower() == correct_ans.lower() :
            score += 1
            print("Correct !")
        else: 
            print(f"Wrong ! Correct ans is {que['answer']}")

    print("\nQuiz finished !\n")
    print(f"Your Score is {score}/{len(questions)}")

quiz()