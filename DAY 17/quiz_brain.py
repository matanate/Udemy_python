import os


class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_q(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(
            f"Q.{self.q_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if (
            correct_answer.lower() == user_answer.lower()
            or user_answer.lower() == correct_answer[0].lower()
        ):
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your score is: {self.score}/{self.q_number}.\n\n")
