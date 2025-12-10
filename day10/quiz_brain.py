class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False)?: ").lower()
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_a, question_a):
        if user_a == question_a.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {question_a}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")