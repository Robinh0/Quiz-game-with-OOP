from question_model import Question
from data import question_data
from quiz_brain import *

def create_question_bank():
    question_bank = []
    for question in question_data:
        question_text = question['question']
        question_answer = question['correct_answer']
        question_object = Question(question_text, question_answer)
        question_bank.append(question_object)
    return question_bank

question_bank = create_question_bank()

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print('Out of questions. Well played!')
print(f'Your final score is {quiz_brain.score} out of {quiz_brain.question_number}.')

