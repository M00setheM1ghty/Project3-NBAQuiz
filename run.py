# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import time
import os
import gspread
from termcolor import colored, cprint
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


# termcolor functions
def print_red(x):
    """
    termcolor functions
    """
    cprint(x, 'red')


def print_green(x):
    """
    termcolor functions
    """
    cprint(x, 'green')


def print_blue(x):
    """
    termcolor functions
    """
    cprint(x, 'blue')


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
        print_red('Oops. Something went wrong')
        time.sleep(3)
        home_screen()
    display_final_score(score)
   

def home_screen():
    """
    displays options: 1: play game, 2: how to play, 3: study material
    """
    cls()
    print(' ')
    print('Welcome to my NBA Finals quiz game!\n')
    print_green('x Play Game')
    print_red('y Rules Explanation')
    print_blue('z Study for the quiz')
    print(' ')

    choice = input('Pick x, y or z:\n')
    choice = choice.lower().replace(" ", "")
    if choice == 'x':
        time.sleep(1)
        play_game()
    elif choice == 'y':
        time.sleep(1)
        display_rules()
    elif choice == 'z':
        time.sleep(1)
        display_data()
    else:
        print_red('You have to choose a valid input! (x,y or z)')
        home_screen()


def display_data():
    """
    display the data questions will be asked about
    """
    cls()
    print('Here you can study the material the questions are about:')
    print(' ')

    data_rows = wsheet.get_all_values()
    for row in data_rows:
        print(row)

    ready_loop()


def display_rules():
    """
    explains the rules of the game
    """
    cls()
    print(' ')
    print_green('The rules are simple:')
    print_red('You will be asked questions.')
    print_blue('You type your answers in. Press enter to confirm your choice.')
    print('You gotta get as many correct as possible.')
    print_green('Good luck!')
    print(' ')
    
    ready_loop()


def game_settings():
    """
    explain the game and start quiz when player is ready
    """
    cls()
    print(' ')
    print_green('Welcome!')
    print_red('This quiz will test your knowledge about the NBA.')
    data_str = input('Are you ready? Y/N:\n')

    if data_str.lower() == 'y':
        print_blue('Let us start quizzing!')
        time.sleep(2)
        difficulty = set_difficulty()
        question_amount = set_question_amount()
        question_index = set_question_index(difficulty)
    elif data_str.lower() == 'n':
        print_blue('Back to the homescreen!')
        home_screen()
    else:
        print_red('Invalid input!')
        time.sleep(1)
        play_game()
    return question_amount, question_index, difficulty


def set_difficulty():
    """
    set game difficulty
    """
    cls()
    print(' ')
    print_green('Rookie')
    print_blue('Amateur')
    print_red('Pro')
    print(' ')
    difficulty_str = input('Which difficulty level would you like to play?\n')
    
    difficulty = ''
    if difficulty_str.lower().strip() == 'rookie':
        difficulty += 'rookie'
    elif difficulty_str.lower().strip() == 'amateur':
        difficulty += 'amateur'
    elif difficulty_str.lower().strip() == 'pro':
        difficulty += 'pro'
    else:
        print_red('Your input is not valid. Try again')
        time.sleep(2)
        set_difficulty()
    return difficulty


def set_question_amount():
    """
    set amount of questions to be asked
    """
    cls()
    print(' ')
    try:
        print(' ')
        print_green('4')
        print_blue('8')
        print_red('12')
        print(' ')

        length_str = int(input('Choose a question amount to answer:\n'))

        question_amount = 0
        if length_str == 4:
            question_amount = 4
        elif length_str == 8:
            question_amount = 8
        elif length_str == 12:
            question_amount = 12
        else:
            print_red('Your input is not valid. Try again:')
            set_question_amount()
        return question_amount
    except ValueError:
        print_red('You need to enter a correct value! (4,8 or 12)')
        time.sleep(1)
        set_question_amount()


def set_question_index(difficulty):
    """
    set the question index to retrieve a random line from the database
    """
    time.sleep(1)
    question_index = 0
    if difficulty == 'rookie':
        question_index = random.randint(40, 57)
    elif difficulty == "amateur":
        question_index = random.randint(21, 39)
    elif difficulty == "pro":
        question_index = random.randint(2, 20)
    else:
        print_red('Oops. something went wrong here.')
        home_screen()
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
    #print(answer_list)

    for count, question in enumerate(question_list, start=1):
        print(' ')
        answer = str(input(f'{question}'+ f' in {year}?\n').lower().replace(" ", ""))
        correct_answer = str(answer_list[count].lower().replace(" ", ""))
        
        if answer == correct_answer:
            print_green('Correct!\n')
            correct_answer_amount += 1
        elif answer != correct_answer:
            print_red('False!')
            print_green(f'Correct Answer: {answer_list[count]}\n')
        else:
            home_screen()
    return correct_answer_amount


def display_final_score(score):
    """
    display final score and message
    """
    time.sleep(1)
    print(' ')
    print(colored('All question answered!', 'blue'))
    print_green(f'Correct Answers: {score}\n ')
    data_str = input('Would you like to play again? Y/N:\n ')

    if data_str.lower() == 'y':
        print_blue('Let\'s go!')
        play_game()
    else:
        print_blue('Back to the homescreen!')
        home_screen()


def cls():
    """
    clear console of old print statements
    """
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def ready_loop():
    """
    asks the user if he is ready to proceed and gives to options to continue
    used to connect different parts of the quiz
    prevents the user from getting stuck with wrong input 
    resets to the homescreen after 3 tries
    """
    time.sleep(1)
    count = 0
    while count < 3:
        print(' ')
        data_str = input('Are you ready? Y/N:\n')

        if data_str.lower() == 'y':
            print_blue('Let\'s go!')
            play_game()
        elif data_str.lower() == 'n':
            print_blue('Back to the homescreen!')
            home_screen()
        else:
            print_red('You have to give a valid input! (Y or N)')
        count += 1
    home_screen()
    time.sleep(2)


home_screen()