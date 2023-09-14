
# NBA Finals Quiz

### A fun little quiz testing your knowledge about basketball's best league.   
### How many questions can you get right?    
      

### Link to the finished game: https://nbaquiz-710fcd41abac.herokuapp.com/
_____________________________________________________________________________
## Content:
- ### Wireframe and project goals 
    - [Lucid Chart](#lucid-chart)
    - [Project Goals and Audience](#project-goals-and-target-audience)
- ### Design and UX
    - [How to play](#how-to-play)
    - [Colour Scheme](#colour-scheme)
    - [User Experience](#user-experience-ux)
        - [First-time Visitor](#first-time-visitor-goals)
        - [Returning Visitor](#returning-visitor-goal)
    - [Typography](#typography)
- ### Technologies Used
    - [Languages used](#languages)
    - [Frameworks, Packages & Programs Used](#frameworks-packages--programs-used)
- ### Testing
    - [PEP8](#pep8)
    - [W3 HTML Checker](#w3-html-checker)
    - [CSS Checker](#w3-css-checker)
    - [Contrast Checker](#contrast-checker)
    - [Lighthouse](#lighthouse)
    - [Bug testing](#bug-testing)
    - [Responsiveness](#responsiveness-and-further-testing)
    - [Fixed bugs](#fixed-bugs)
- ### Deployment
    - [Deploy to Heroku](#deployment)
- ### Credits
    - [Code](#code)
    - [Content](#contents)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)



_____________________________________________________________________________
## Lucid chart
![Screenshot](/images/lucidchart.png)  
_____________________________________________________________________________ 
## Project goals and target audience.  
### Achieved:
- Build a quiz game that asks different questions depending on your decisions on game length and difficulty.
- Tracks score in the game played.
- Be easy to understand and navigate.
- Make it colorful so it is easy to read give it some contrast. 

### Future projects: 
- Add more questions and different topics to make the game different every time.
- Take names from players and keep the scores in the database. (e.g all time questions answered, all time correct answers etc.)    

## Audience:
- This game is for everyone, since the given topic can be studied in the game. 
- I suppose it is more fun for sports or specifically for people interested in basketball.   
_____________________________________________________________________________ 
### Design and UX
## How to play:   
- choose between the given options to navigate through the quiz
- try different difficulty levels
- 3 different game lenghts to choose from
- answer the questions and see how many you can get correct
_____________________________________________________________________________  
## Colour Scheme
- I used termcolor to print text in different colors: red, blue, green. 
- The standard terminal ouput(white) contrasts nicely with the rest and the black background.
- This insures readability and proper contrast 
_____________________________________________________________________________  
## User Experience (UX)   

### First-Time Visitor Goals
- Object and type of the game are obvious and easy to pursue
- play easy and short games to get the hang of the game

### Returning Visitor Goal
- study given material to achieve better scores
- try harder and higher amount of questions 

## Typography
- Standard terminal output
- Added colors with termcolor
_____________________________________________________________________________  
## Languages
- HTML5 from CodeInstitute Template
- CSS from CodeInstitute Template
- Javascript from CodeInstitute Template
- Python code written by me ;D
____________________________________________________________________________  
## Frameworks, Packages & Programs Used
- Lucidchart to provide a flowchart to explain the program
- Google Sheets + API to access the data necessary for the questions
- Packages used:
    - random (needed random numbers to make sure questions asked are random)
    - time (added some sleep periods in the program to make the experience less jumpy)
    - os (to be able to clear the terminal)
    - gspread (access google sheets)
    - termcolor: cprint, colored   
____________________________________________________________________________  
## Testing

### PEP8

- no errors found with the pep8 linter:\
![Screenshot](/images/pep8P3.png)

### W3 HTML Checker 

- no issues in the W3 html validator\
![Screenshot](/images/w3-validation-p3.png)

### Bug testing
|   Item    |    Bug     |   Fix    |
|---|---|---|
|  input fields   | crashing the program when enter was pressed directly without input | added steps in the functions to validate input and restart if necessary  |
|  ask_questions()  |  if 8 or 12 questions are asked the questions were the same for questions 5-12  |  reset the question index when calling function again  |
|  set_difficulty()    |  was very strict with the input -> not accepting spaces before and after the word, lower and upper case sensitive   |  converted string input to lowercase and stripped the spaces before validation   |
|  ask_questions()  | was very strict with the input -> not accepting spaces before and after the word, lower and upper case sensitive  | converted string input to lowercase and stripped the spaces before validation  |
|  repeating code   |  was using the same code to ask the user to continue multiple times |  refactored it into function ready_loop()  |
|  transitions between the quiz elements   | happened way to fast -> messages were deleted to quickly -> user could not read them | added breaks with the time.sleep() function, specifically in the function cls() which clears the terminal  |
|  ask_questions()  | comparing given answer to correct answer gave false even though input was correct  |  data in google sheets had different type of the character - somehow -> changed it to -- to be the same in answer validation  |
|  set_question_amount() |  question amount 8 and 12 sometimes throw range parsing errors that crash the program |  added try except block that restarts the function in the error case  |

### Unfixed Bugs

 - Sometimes when choosing the question amount in game_settings() the program throws a parsing Error. I could not find the reason why. Also it rarely happens. I go around it by having a loop in place that restarts the game at a specific point if it crashes.  

### Responsiveness and Further Testing

## Am I responsive image 
![Screenshot](/images/amiresponsiveP3.png)

- scales fine on different screen sizes
- runs in chrome, edge and firefox browser
_____________________________________________________________________________  

## Deployment
### How to use the provided template
- fork the p3-template provided by CodeInstitute: https://github.com/Code-Institute-Org/p3-template \
![Screenshot](/images/usetemplateP3.png)
- give the repo a name and click "Create repository":\
![Screenshot](/images/newrepoP3.png)

### Deploying the App in Heroku
- deployed via the heroku platform
- homepage -> create app -> choose country and app name
- add necessary build packs and config variables in settings:

Build packs:
1. `heroku/python`
2. `heroku/nodejs`

Config Vars:
`PORT` `8000`
`CREDS` `the contents of the creds.json file`

- under deploy at the bottom of the page click: DEPLOY
_____________________________________________________________________________  

## Credits.  

### Code.
- How to clear the console of old prints:
https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console

- how to use termcolor
https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b

- markdown cheatsheet
https://markdown.land/markdown-cheat-sheet

- how to force pauses in the program:
https://realpython.com/python-sleep/

### Contents  
- dataset used for the question answers:
https://www.kaggle.com/datasets/thedevastator/historical-nba-finals-and-mvp-results?resource=download

- lucid chart to create the flowchart for the program
https://www.lucidchart.com/pages/

### Media  
- ASCII art provided by:
https://www.asciiart.eu/sports-and-outdoors/basketball

### Acknowledgements

The projects done by other students of my mentor helped me build the finished program and gave me good inspiration and pointers on how to execute my ideas. 
https://github.com/CluelessBiker/mentoring/blob/main/sample-projects.md
_____________________________________________________________________________   