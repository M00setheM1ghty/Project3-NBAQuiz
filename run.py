# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import os
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
    cls()
    question_amount, question_index, difficulty = game_settings()
    score = 0
    if question_amount == 4:
        score += ask_questions(question_index)
    elif question_amount == 8:
        score += ask_questions(question_index)
        question_index = set_question_index(difficulty)
        score += ask_questions(question_index)
    elif question_amount == 12:
        score += ask_questions(question_index)
        question_index = set_question_index(difficulty)
        score += ask_questions(question_index)
        question_index = set_question_index(difficulty)
        score += ask_questions(question_index)
    else:
        print('Oops. Something went wrong')
        home_screen()
    display_final_score(score)
   

def home_screen():
    """
    displays options: 1: play game, 2: how to play
    """
    cls()
    print(' ')
    print('Welcome to my NBA Finals quiz game!\n')
    print('x Play Game')
    print('y Rules Explanation')
    print('z Study for the quiz')
    print(' ')

    choice = input('Pick x, y or z:\n')
    if choice == 'x':
        play_game()
    elif choice == 'y':
        display_rules()
    elif choice == 'z':
        display_data()
    else:
        print('You have to choose one!')
        home_screen()


def display_data():
    """
    display the data questions will be asked about
    """
    cls()
    print('Here you can study the material asked in the questions:')
    print(' ')

    data_rows = wsheet.get_all_values()
    for row in data_rows:
        print(row)

    


def display_rules():
    """
    explains the rules of the game
    """
    cls()
    print(' ')
    print('The rules are simple:')
    print('You will be asked questions.')
    print('You type your answers in. Press enter to confirm your choice.')
    print('You gotta get as many correct as possible.')
    print('Good luck!')
    print(' ')
    
    data_str = input('Are you ready? Y/N:\n')

    if data_str.lower() == 'y':
        print('Let\'s go!')
        play_game()
    else:
        print('Back to the homescreen!')
        home_screen()


def game_settings():
    """
    explain the game and start quiz when player is ready
    """
    cls()
    print(' ')
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
    cls()
    print(' ')
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
    cls()
    print(' ')
    try:
        length_str = int(input('How many questions would you like to answer? 4/8/12\n'))
        question_amount = 0
        if length_str == 4:
            question_amount = 4
        elif length_str == 8:
            question_amount = 8
        elif length_str == 12:
            question_amount = 12
        else:
            print('Your input is not valid. Try again:')
            set_question_amount()
        return question_amount
    except ValueError:
        print('You need to enter a correct value! (4,8 or 12)')


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
    cls()
    correct_answer_amount = 0
    answer_list = wsheet.row_values(question_index)
    question_list = question_sheet.col_values(1)
    year = answer_list[0]
    print(answer_list)

    for count, question in enumerate(question_list, start=1):
        answer = str(input(f'{question}'+f' in {year}?\n').lower().replace(" ", ""))
        correct_answer = str(answer_list[count].lower().replace(" ", ""))
        
        if answer == correct_answer:
            print('Correct!\n')
            correct_answer_amount += 1
            # print(answer_list[count])
            print(count)
        elif answer != correct_answer:
            print('False!')
            print(f'Correct Answer: {answer_list[count]}\n')
        else:
            home_screen()
    return correct_answer_amount


def display_final_score(score):
    """
    display final score and message
    """
    print(' ')
    print('All question answered!')
    print(f'Correct Answers: {score}\n ')
    data_str = input('Would you like to play again? Y/N:\n ')

    if data_str.lower() == 'y':
        print('Let\'s go!')
        play_game()
    else:
        print('Back to the homescreen!')
        home_screen()


def cls():
    """
    clear console of old print statements
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def ready_loop():
    """
    asks the user if he is ready to proceed and gives to options to continue
    used to connect different parts of the quiz
    """
    print(' ')
    data_str = input('Are you ready? Y/N:\n')

    if data_str.lower() == 'y':
        print('Let\'s go!')
        play_game()
    elif data_str.lower() == 'n':
        print('Back to the homescreen!')
        home_screen()
    else:
        while count < 3:
            print('You have to give a valid input! (Y or N)')
            
            count += 1


home_screen()