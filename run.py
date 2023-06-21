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

def set_length():
    """
    set game length
    """
def create_question():
    """
    create question from the NBA finals spreadsheet
    """    

play_game()
