class QuizBrain:

    def __init__(self, question_list):
        self.questions = question_list
        self.question_number = 0
        self.guessed = 0

    def stillHasQuestions(self):
        return self.question_number < len(self.questions) - 1
    def next_question(self):

        question = self.questions[self.question_number]
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.question_number += 1
        result = answer.lower() == question.answer.lower()
        if result:
            print("You got it right!")
            self.guessed += 1
        else:
            print("You didn't guess it!")
        print(f"The correct answer was {question.answer}. Your current score is {self.guessed}/{self.question_number}")
        return result
