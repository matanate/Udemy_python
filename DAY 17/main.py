from question_model import Question
from data import create_question_data
from quiz_brain import QuizBrain
import os

os.system("cls")
question_bank = []
q_number = input("Choose the number of questions: ")
os.system("cls")
question_data = create_question_data(q_number)
for q in question_data:
    q_text = q["question"]
    q_answer = q["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_q():
    quiz.next_question()
os.system("cls")
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.q_number}")
input("Press Enter to exit.")
