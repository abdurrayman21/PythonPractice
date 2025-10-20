#lsit of questions
#store answers
#Random questions
#track score
#tell if answer is correct or not
#show total score
import random
questions = {
    "What keyword is used to create a class in Python?": "class",
    "Which method is called when an object is created in Python classes?": "__init__",
    "What is the output of len([1, 2, 3]) in Python?": "3",
    "Which operator is used for string concatenation in Python?": "+",
    "What is the correct way to create a list in Python?": "[]",
    "What data structure uses key-value pairs in Python?": "dictionary",
    "Which function is used to find the maximum value in a list?": "max",
    "What is the output of type(10) in Python?": "<class 'int'>",
    "How do you write a multi-line comment in Python?": "'''",
    "What keyword is used to handle exceptions in Python?": "try",
    "Which function converts a string to lowercase?": "lower",
    "What does the 'break' statement do in Python loops?": "exits loop",
    "Which method adds an element to the end of a list?": "append",
    "What is the correct syntax for an if statement in Python?": "if condition:",
    "Which keyword is used to check if a value exists in a list?": "in",
    "What is the output of 5 % 2 in Python?": "1",
    "Which built-in function returns the absolute value of a number?": "abs",
    "What is the result of bool(0) in Python?": "False",
    "Which function converts a value to an integer?": "int",
    "How do you create a tuple in Python?": "()"
}

def python_trivea_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Enter your answer: ").lower().strip()
        correct_answer = questions[question]
        if user_answer == correct_answer.lower():
            print("correct\n")
            score +=1
        else:
            print(f"wrong\n the correct answer is {correct_answer}.\n")
python_trivea_game()