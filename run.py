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
    create_questions()


def display_start_screen():
    """
    explain the game and start quiz when player is ready
    """
    print('Welcome!\nThis quiz will be testing your knowledge on the NBA basketball finals.')
    data_str = input('Are you ready? Y/N:\n')

    if data_str == 'Y' or data_str == 'y':
        print('Let us start quizzing!')
    else:
        print('Back to the homescreen!')


def set_difficulty():
    """
    set game difficulty
    """
    difficulty_str = input('How hard do you want this to be? ROOKIE/AMATEUR/PRO')
    if difficulty_str == 'ROOKIE':
        pass
    elif difficulty_str == 'AMATEUR':
        pass
    elif difficulty_str == 'PRO':
        pass
    else: 
        print('Your input is not valid. Try again')
        set_difficulty()
    
def set_length():
    """
    set amount of questions to be asked
    """
    length_str = input('How many questions would you like to answer? 5/10/15')
    if int(length_str) == 5:
        pass
    elif int(length_str) == 10:
        pass
    elif int(length_str) == 15:
        pass
    else:
        print('Your input is not valid. Try again')
        


def create_questions():
    """
    create question from the NBA finals spreadsheet
    """
    #question_index = random.randint(1, 69)


play_game()
