import random
import time
import os
import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored
import cosmetics

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
    calls the functions to go through the questions
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
        cosmetics.print_red('Oops. Something went wrong')
        time.sleep(3)
        home_screen()
    display_final_score(score)


def home_screen():
    """
    starting screen
    displays options: 1: play game, 2: how to play, 3: study material
    """
    cls()
    cosmetics.art_0()
    print(' ')
    print('    Welcome to my NBA Finals quiz game!\n')
    cosmetics.print_green('    x Play Game')
    cosmetics.print_red('    y Rules Explanation')
    cosmetics.print_blue('    z Study for the quiz')
    print(' ')

    choice = input('    Pick x, y or z:\n')
    choice = choice.lower().replace(" ", "")
    if choice == 'x':
        time.sleep(0.5)
        play_game()
    elif choice == 'y':
        time.sleep(0.5)
        display_rules()
    elif choice == 'z':
        time.sleep(0.5)
        display_data()
    else:
        cosmetics.print_red('    You have to choose a valid input! (x,y or z)')
        home_screen()


def display_data():
    """
    display the data questions will be asked about
    """
    cls()
    cosmetics.art_2()
    print('    Here you can study the material the questions are about:')
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
    cosmetics.art_3()
    print(' ')
    cosmetics.print_green('    The rules are simple:')
    cosmetics.print_red('    You will be asked questions')
    cosmetics.print_blue('    Type your answers in. Press enter to confirm')
    print('    You gotta get as many correct as possible.')
    cosmetics.print_green('    Good luck!')
    print(' ')

    ready_loop()


def game_settings():
    """
    explains the subject game and start quiz when player is ready
    """
    cls()
    cosmetics.art_4()
    print(' ')
    cosmetics.print_green('    Welcome!')
    cosmetics.print_red('    This quiz will test your knowledge about the NBA')
    data_str = input('    Are you ready? Y/N:\n')

    if data_str.lower() == 'y':
        cosmetics.print_blue('    Let us start quizzing!')
        time.sleep(2)
        difficulty = set_difficulty()
        question_amount = set_question_amount()
        question_index = set_question_index(difficulty)
    elif data_str.lower() == 'n':
        cosmetics.print_blue('    Back to the homescreen!')
        home_screen()
    else:
        cosmetics.print_red('    Invalid input!')
        time.sleep(1)
        play_game()
    return question_amount, question_index, difficulty


def set_difficulty():
    """
    set game difficulty
    """
    cls()
    cosmetics.art_5()
    print(' ')
    cosmetics.print_green('    Rookie')
    cosmetics.print_blue('    Amateur')
    cosmetics.print_red('    Pro')
    print(' ')
    difficulty_str = input(
        '    Which difficulty level would you like to play?\n'
    )

    difficulty = ''
    if difficulty_str.lower().strip() == 'rookie':
        difficulty += 'rookie'
    elif difficulty_str.lower().strip() == 'amateur':
        difficulty += 'amateur'
    elif difficulty_str.lower().strip() == 'pro':
        difficulty += 'pro'
    else:
        cosmetics.print_red('    Your input is not valid. Try again')
        time.sleep(1)
        set_difficulty()
    return difficulty


def set_question_amount():
    """
    set amount of questions to be asked
    """
    cls()
    cosmetics.art_6()
    print(' ')
    try:
        print(' ')
        cosmetics.print_green('    4')
        cosmetics.print_blue('    8')
        cosmetics.print_red('    12')
        print(' ')

        length_str = int(
            input('    Choose a question amount to answer:\n')
        )

        question_amount = 0
        if length_str == 4:
            question_amount = 4
        elif length_str == 8:
            question_amount = 8
        elif length_str == 12:
            question_amount = 12
        else:
            cosmetics.print_red('    Your input is not valid. Try again:')
            set_question_amount()
        return question_amount
    except ValueError:
        cosmetics.print_red(
            '    You need to enter a correct value! (4,8 or 12)'
        )
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
        cosmetics.print_red('    Oops. something went wrong here.')
        home_screen()
    return question_index


def ask_questions(question_index):
    """
    creating and displaying the questions with the provided list
    """
    cls()
    cosmetics.art_1()
    correct_answer_amount = 0
    answer_list = wsheet.row_values(question_index)
    question_list = question_sheet.col_values(1)
    year = answer_list[0]

    for count, question in enumerate(question_list, start=1):
        print(' ')
        answer = str(input(
            f'    {question}' +
            f' in {year}?\n').lower().replace(" ", "")
        )
        correct_answer = str(answer_list[count].lower().replace(" ", ""))

        if answer == correct_answer:
            cosmetics.print_green('    Correct!\n')
            correct_answer_amount += 1
        elif answer != correct_answer:
            cosmetics.print_red('    False!')
            cosmetics.print_green(
                f'    Correct Answer: {answer_list[count]}\n'
            )
        else:
            home_screen()
    return correct_answer_amount


def display_final_score(score):
    """
    display final score and message
    """
    cls()
    time.sleep(0.5)
    print(' ')
    print(colored('    All question answered!', 'blue'))
    cosmetics.print_green(f'    Correct Answers: {score}\n ')
    data_str = input('    Would you like to play again? Y/N:\n')

    if data_str.lower() == 'y':
        cosmetics.print_blue('    Let\'s go!')
        play_game()
    else:
        cosmetics.print_blue('    Back to the homescreen!')
        home_screen()


def cls():
    """
    clear console of old print statements
    """
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')


def ready_loop():
    """
    asks the user if he is ready to proceed and gives to options to continue
    used to connect different parts of the quiz
    prevents the user from getting stuck with wrong input
    resets to the homescreen after 3 tries
    """
    time.sleep(0.5)
    count = 0
    while count < 3:
        print(' ')
        data_str = input('    Are you ready? Y/N:\n')

        if data_str.lower() == 'y':
            cosmetics.print_blue('    Let\'s go!')
            play_game()
        elif data_str.lower() == 'n':
            cosmetics.print_blue('    Back to the homescreen!')
            home_screen()
        else:
            cosmetics.print_red('    You have to give a valid input! (Y or N)')
        count += 1
    home_screen()
    time.sleep(1)


home_screen()
