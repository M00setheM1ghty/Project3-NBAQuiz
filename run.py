# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
import random
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
    calls the necessary functions to go through the game
    """
    display_start_screen()
    set_difficulty()
    set_question_amount()
    create_questions()


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
        question_amount += 5
    elif int(length_str) == 10:
        question_amount += 10
    elif int(length_str) == 15:
        question_amount += 15
    else:
        print('Your input is not valid. Try again')    
    return question_amount
    

def create_questions():
    """
    create question from the NBA finals spreadsheet
    """
    #question_index = random.randint(2, 64)


play_game()
