Q1 = {
    'question' : "What is the latest Windows OS?",
    'answers' : "1. Windows-X 2. Windows-10 3. Windows-Cleaned",
    'correct_answer' : "2"
}

Q2 = {
    'question' : "How do I open the start menu in Win 10?",
    'answers' : "1. The Win Icon 2. Ask Nicely 3. You don't",
    'correct_answer' : "1"
}

print(Q1['question'])

def ask_questions():

    questions_array = [Q1, Q2]

    array_length = len(questions_array)

    correct_answers = 0

    for x in range(0, array_length):
        print(questions_array[x]['question'])
        print(questions_array[x]['answers'])
        answer = input()
        if answer == (questions_array[x]['correct_answer']):
            print("Correct")
            correct_answers = correct_answers + 1
        elif answer != (questions_array[x]['correct_answer']):
            print("Incorrect")
    
    print(correct_answers)
