Q1 = {
    'question' : "What is the latest Windows OS?",
    'answers' : "1. Windows-X 2. Windows-10 3. Windows-Cleaned",
    'correct_answer' : "2"
}

print(Q1['question'])

def ask_questions():

    correct_answers = 0

    print(Q1['question'])
    print(Q1['answers'])
    answer = input()
    if answer == (Q1['correct_answer']):
        print("Correct")
        correct_answers = correct_answers + 1
    elif answer != (Q1['correct_answer']):
        print("Incorrect")
    
    print(correct_answers)
