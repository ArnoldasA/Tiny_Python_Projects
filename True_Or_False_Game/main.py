from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# create the question bank
# should contain a list of question objects
# Each being initialized with a question and answer
# text and answer
# Random selection of question
# Or we could go iteratively  up the list

list_size = len(question_data)
cur_question = 0

question_bank = []

for questions in question_data:
    answer = questions["answer"]
    text = questions["text"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

while cur_question != list_size:
    lost_game = QuizBrain.lost_game
    print(f"Score:{cur_question} out of {list_size}")
    if lost_game is True:
        break
    else:
        question = question_bank[cur_question].question
        solution = question_bank[cur_question].solution
        QuizBrain(list_size, answer, question, cur_question)
        cur_question += 1

# Question number and question list
