UserAnswers = {
    "language_preferences": None, "country_preferences": None, "user_age": None, # Main Module
    "reading_frequency": None, # OlderThanFive Module
    "day_week_reading_time": None, "reading_place": None, "reading_time": None, "read_fiction_novel_lately": None, # ReadersOnly Module
    "genre_preferences": None, "lead_sexuality": None, # LiteraryGenre Module
    "last_fiction_book_name": None, "last_book_author_name": None # LastBook Module
}


def main_module(question, options):

    options_no_more = options + ["No more"]

    answer = []

    finish = False
    while not finish: 
        print("\nLanguage options: ")
        print("-----------------------------------------------------")
        available_options = {num: option for num, option in enumerate(options_no_more) if option not in answer}
        for num, option in available_options.items():
            print(f"{num}- {option}")
        print("-----------------------------------------------------")

        user_input = input(question).split()
        
        invalid_options = []

        for i in user_input:
            if i.isnumeric():
                i = int(i)
                if i not in available_options.keys():
                    invalid_options.append(i)
                elif i == len(options_no_more) - 1: 
                    if not answer:
                        print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                        print("              Thank you for providing your language preference!              ")
                        print("Since you don't know any of the languages, we cannot recommend you any book.")
                        print("                   We are really sorry to see you go! ˙◠˙                   ")
                        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
                        return 
                    finish = True
                    break
                else:
                    answer.append(options_no_more[i])
            else: 
                if i in available_options.values():
                    answer.append(i)
                else:
                    invalid_options.append(i)

        if invalid_options != []:
            print("\n──────────────────────────────────────────────────────────────────")
            print("The following options are not valid! ¯|_(ツ)_/¯ Please, try again ^^")
            print("Invalid options:", ", ".join(str(i) for i in invalid_options))
            print("──────────────────────────────────────────────────────────────────")

    return answer

language_options = [
    "arabic", "chinese", "english", "french", "german", "hindi",
    "japanese", "portuguese", "russian", "spanish", "swahili"]

question = "Which languages do you know and prefer to read? \
            \nChoose them one by one (or multiple separated by a space): "

print(main_module(question, language_options))


import json

# Assuming you have a JSON file named 'data.json'
file_path = './Code/Python/Data/texts.json'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)
print(data)