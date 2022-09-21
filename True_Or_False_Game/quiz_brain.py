class QuizBrain:
    lost_game = False

    def __init__(self, questions_list, answer, questions, question_number):
        self.cur_num = question_number
        self.question_num = question_number
        self.overall_questions = questions_list
        self.answer = answer
        self.question = questions

        while question_number != questions_list:
            print(f"Q.{question_number}:{questions}:True or False")
            user_input = input("")
            if user_input == answer:
                print("Correct!\nNext Question")
                break;
            else:
                print("Incorrect!\nYou Lose!")
                QuizBrain.lost_game = True
                break;


