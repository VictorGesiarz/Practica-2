
class MultipleChoiceQuestion:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

    def ask_question(self):
        print(self.question)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

# Example usage
question_1 = MultipleChoiceQuestion(
    "What is the capital of France?",
    ["Berlin", "Paris", "Madrid", "Rome"],
    2
)

question_2 = MultipleChoiceQuestion(
    "Which programming language is this code written in?",
    ["Python", "Java", "C++", "JavaScript"],
    1
)

question_1.ask_question()
user_answer_1 = int(input("Enter your answer: "))
result_1 = question_1.check_answer(user_answer_1)
print("Correct!" if result_1 else "Incorrect.")

question_2.ask_question()
user_answer_2 = int(input("Enter your answer: "))
result_2 = question_2.check_answer(user_answer_2)
print("Correct!" if result_2 else "Incorrect.")
