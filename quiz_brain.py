class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input("Q {question_nr}: {question} 'True' or 'False'?\n"
                       .format(question_nr=(self.question_number + 1),
                               question=current_question.text)).lower()
        self.print_score(answer, current_question)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def print_score(self, answer, current_question):
        if answer.lower() == current_question.answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('You got it wrong.')
        print(f'The correct answer was {current_question.answer.lower()}')
        print(f"Your current score: {self.score}/{self.question_number + 1}")
        print('\n')

