Q1 = {
    'question' : "What is your name?",
    'answers' : "1. Steve 2. Jake 3. Billy",
    'correct_answer' : "2"
}


print(Q1['question'])

def ask_questions():

    print(Q1['question'])
    print(Q1['answers'])
    answer = input()
    if answer == (Q1['correct_answer']):
        print("Correct")




