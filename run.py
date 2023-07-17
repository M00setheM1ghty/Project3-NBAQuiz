# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('NBAFinalsData')

wsheet = SHEET.worksheet('QuestionAnswers')
question_sheet = SHEET.worksheet('QuestionTemplates')


def play_game():
    """
    calls the functions to go through the game
    """
    question_amount, question_index, difficulty = game_settings()
    #print(type(question_index))
    #boprint(type(question_amount))
    if question_amount == 4:
        ask_questions(question_index)
    elif question_amount == 8:
        ask_questions(question_index)
        question_index = set_question_index(difficulty)
        ask_questions(question_index)
    elif question_amount == 12:
        ask_questions(question_index)
        question_index = set_question_index(difficulty)
        ask_questions(question_index)
        question_index = set_question_index(difficulty)
        ask_questions(question_index)
    else:
        print('Oops. Something went wrong')
        home_screen()
    #correct, wrong = track_score()
    #display_final_score(correct, wrong)


def home_screen():
    """
    displays options: 1: play game, 2: how to play
    """
    print('Welcome to my quiz game!')
    print('x Play Game')
    print('y Rules Explanation')

    choice = input('Pick x or y:\n')
    if choice == 'x':
        play_game()
    elif choice == 'y':
        display_rules()
    else:
        print('You have to choose one!')
        home_screen()


def display_rules():
    """
    explains the rules of the game
    """
    print('The rules are simple:')
    print('You will be asked questions.')
    print('You type your answers in.')
    print('You gotta get as many correct as possible.')
    print('Good luck!')
    data_str = input('Are you ready? Y/N:\n')

    if data_str.lower() == 'y':
        print('Let\'s go!')
    else:
        print('Back to the homescreen!')
        home_screen()


def game_settings():
    """
    explain the game and start quiz when player is ready
    """
    print('Welcome!\nThis quiz will be testing your knowledge on the NBA basketball finals.')
    data_str = input('Are you ready? Y/N:\n')

    if data_str.lower() == 'y':
        print('Let us start quizzing!')
        difficulty = set_difficulty()
        question_amount = set_question_amount()
        question_index = set_question_index(difficulty)
    else:
        print('Back to the homescreen!')
        home_screen()
    return question_amount, question_index, difficulty


def set_difficulty():
    """
    set game difficulty
    """
    difficulty_str = input('Which difficulty level?\nRookie/Amateur/Pro:\n')
    difficulty = ''
    if difficulty_str.lower().strip() == 'rookie':
        difficulty += 'rookie'
    elif difficulty_str.lower().strip() == 'amateur':
        difficulty += 'amateur'
    elif difficulty_str.lower().strip() == 'pro':
        difficulty += 'pro'
    else:
        print('Your input is not valid. Try again')
        set_difficulty()
    return difficulty


def set_question_amount():
    """
    set amount of questions to be asked
    """
    length_str = input('How many questions would you like to answer? 4/8/12\n')
    question_amount = 0
    if int(length_str) == 4:
        question_amount = 4
    elif int(length_str) == 8:
        question_amount = 8
    elif int(length_str) == 12:
        question_amount = 12
    else:
        print('Your input is not valid. Try again:')
        set_question_amount()
    return question_amount


def set_question_index(difficulty):
    """
    set the question index to retrieve a random line from the database
    """
    question_index = 0
    if difficulty == 'rookie':
        question_index = random.randint(40, 57)
    elif difficulty == "amateur":
        question_index = random.randint(21, 39)
    elif difficulty == "pro":
        question_index = random.randint(2, 20)
    else:
        print('Oops. something went wrong here.')
    return question_index


def ask_questions(question_index):
    """
    creating and displaying the questions with the provided list
    """
    answer_list = wsheet.row_values(question_index)
    question_list = question_sheet.col_values(1)
    year = answer_list[0]
    print(year)
    print(answer_list)
    print(question_list)

    for count, question in enumerate(question_list, start=1):
        answer = str(input(f'{question}'+f' in {year}?\n').lower().replace(" ", ""))
        correct_answer = str(answer_list[count].lower().replace(" ", ""))

        if answer == correct_answer:
            #track_score(answer, correct_answer)
            print(answer)
            print(correct_answer)
            print(type(answer))
            print(type(correct_answer))
            print('Correct!')
            # print(answer_list[count])
            print(count)
        elif answer != correct_answer:
            #print(str(answer.lower().strip()))
            #print(answer_list[count].lower().replace(" ", ""))
            print(answer)
            print(correct_answer)
            print(type(answer))
            print(type(correct_answer))
            print('False!')
            print(f'Correct Answer: {answer_list[count]}')
            print(count)
        else:
            home_screen()
            
# somethin still goes wrong when asking for game result: prints false even if answer is correct


def track_score(answer, correct_answer):
    """
    tracks and increments correct and wrong answers
    """
    correct = 0
    wrong = 0

    if answer == correct_answer:
        correct += 1
    else:
        wrong += 1

    return correct, wrong


def display_final_score(correct, wrong):
    """
    display final score and message
    """
    print('All question answered!')
    print('Here is your score:')
    print(f'Correct:{correct}\n')
    print(f'Wrong:{wrong}\n')


home_screen()