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
    display_start_screen()
    difficulty = set_difficulty()
    question_amount = set_question_amount()
    question_index = set_question_index(difficulty)
    create_questions(question_index)


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
    length_str = input('How many questions would you like to answer? 4/8/12\n')
    question_amount = 0
    if int(length_str) == 4:
        question_amount = 4
    elif int(length_str) == 8:
        question_amount = 8
    elif int(length_str) == 12:
        question_amount = 12
    else:
        print('Your input is not valid. Try again')
        set_question_amount()
    return question_amount


def set_question_index(difficulty):
    """
    set the question index to retrieve a random line from the database
    """
    question_index = 0
    if difficulty == 'rookie':
        question_index = random.randint(50, 64)
    elif difficulty == "amateur":
        question_index = random.randint(30, 49)
    elif difficulty == "pro":
        question_index = random.randint(1, 29)
    else:
        print('Oops. something went wrong here.')
    return question_index


def create_questions(question_index):
    """
    displaying the question with the provided list
    """
    info_list = wsheet.row_values(question_index)
    question_list = question_sheet.col_values(1)
    year = int(info_list[0])
    print(year)
    print(info_list)
    print(question_list)
    

play_game()
