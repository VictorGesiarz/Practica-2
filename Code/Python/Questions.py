

class UserInteraction():
    
    @staticmethod
    def ask_single_choice_question(question, choices):
        choices_str = " / ".join([f'{choice} ({i+1})' for i, choice in enumerate(choices)])
        answer = input(f'{question} {choices_str}\n')
        
        while True:
            if answer.isnumeric():
                answer = int(answer)
            for i, choice in enumerate(choices):
                if answer == i+1 or answer == choice:
                    return choice
            answer = input("That is not a valid choice. Try again: ")

    @staticmethod
    def ask_multiple_choice_question(question, choices):
        choices += ["Done"]
        
        answers = []
        finish = False
        while not finish:

            if choices == ["Done"]:
                return answers

            choices_str = " / ".join([f'{choice} ({i+1})' for i, choice in enumerate(choices)])
            answer = input(f'{question} {choices_str}\n')        
            if answer.isnumeric():
                answer = int(answer)

            print_ = False
            for i, choice in enumerate(choices):
                if answer == "Done" or (i+1 == answer and choice == "Done"):
                    return answers
                elif answer == i+1 or answer == choice:
                    answers.append(choice)
                    choices.remove(choice)
                    break
                print_ = True
            if print_:
                print("Not a valid option.", end=" ")
                print_ = False

    @staticmethod
    def ask_questions():
        ...


print(UserInteraction.ask_multiple_choice_question("Que prefieres?", ["Hola", "Adios", "Comeme_lapicha"]))