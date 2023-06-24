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

wsheet = SHEET.worksheet('NBAFinals')


def play_game():
    """
    calls the functions to go through the game
    """
    display_start_screen()
    difficulty = set_difficulty()
    question_amount = set_question_amount()
    question_index = set_question_index(difficulty)
    create_questions(question_amount, question_index)


def display_start_screen():
    """
    explain the game and start quiz when player is ready
    """
    print('Welcome!\nThis quiz will be testing your knowledge on the NBA basketball finals.')
    data_str = input('Are you ready? Y/N:\n')

    if data_str.lower() == 'y':
        print('Let us start quizzing!')
    else:
        print('Back to the homescreen!')
        display_start_screen()


def set_difficulty():
    """
    set game difficulty
    """
    difficulty_str = input('Which difficulty level?\nRookie/Amateur/Pro:\n')
    difficulty = ''
    if difficulty_str.lower() == 'rookie':
        difficulty += 'rookie'
    elif difficulty_str.lower() == 'amateur':
        difficulty += 'amateur'
    elif difficulty_str.lower() == 'pro':
        difficulty += 'pro'
    else:
        print('Your input is not valid. Try again')
        set_difficulty()
    return difficulty


def set_question_amount():
    """
    set amount of questions to be asked
    """
    length_str = input('How many questions would you like to answer? 5/10/15\n')
    question_amount = 0
    if int(length_str) == 5:
        question_amount = 5
    elif int(length_str) == 10:
        question_amount = 10
    elif int(length_str) == 15:
        question_amount = 15
    else:
        print('Your input is not valid. Try again')    
    return question_amount


def set_question_index(difficulty):
    """
    set the question index to retrieve a random line from the database
    """
    question_index = 0
    if difficulty == 'rookie':
        question_index = random.randint(50, 64)
    elif difficulty == "amateur":
        question_index = random.randint(30, 64)
    elif difficulty == "veteran":
        question_index = random.randint(1, 64)
    else:
        print('Oops. something went wrong here.')
    return question_index


def create_questions(question_amount, question_index):
    """
    create questions with the supllied index and amount
    """
    print(question_index)
    info_list = wsheet.row_values(question_index)
    print(info_list) 


play_game()
