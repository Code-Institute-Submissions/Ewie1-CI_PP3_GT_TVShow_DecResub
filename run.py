# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from questionanswer_lev_one import questions
from questionanswer_lev_one import answers
import random
import sys
import os


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("login.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("login")

login = SHEET.worksheet("login")
data = login.get_all_values()
print(data)

def logo_page():

    """
    print game logo and name
    """

    print( "  __________________    ______________   ____________.__  "  )               
    print(" /  _____\__    ___/    \__    ___\   \ /   /   _____|  |__   ______  _  __")
    print("/   \  ___ |    |  ______ |    |   \   Y   /\_____  \|  |  \ /  _ \ \/ \/ /")
    print("\    \_\  \|    | /_____/ |    |    \     / /        |   Y  (  <_> \     / ")
    print(" \______  /|____|         |____|     \___/ /_______  |___|  /\____/ \/\_/  ")
    print("        \/                                         \/     \/               ")
    print("-" *75)
    print("                      Can you Guess That TV Show \n")

    print("                                                             "f"Your Score:{score}") 



def scores():
    score = 0
    if score < 1000:
        print("Run level 1")
        print("                                                             "f"Your Score:{score}") 
        return True
    elif score >= 1000:
        print("Run level 2")
    elif score >= 2000:
        print("Run level 3")
    elif score == 3000:
        print("End/Restart game")
    else:
        print("end game")

    

def clear_screen():
    """
    Clear screen
    """
    os.system('clear') 


def get_question_answers():

    """
    get questions and answers and print for player input
    """
    for question in questions:
        chances = 3 
    while chances > 0:
        randoms = random.choice([question for question in questions.values()])
        question = randoms["question"]
        print(question)
        question = randoms["answer"]
        print("")
        ans = input("Guess the Show:")
        if check_answer(question, ans, score, chances):
            break
        chances -= 1
                
def check_answer(question, ans, score, chances):
    """
    Check player answer is wrong or correct, 
    print feed back 
    """
    
    if question == ans:
        score = score + 125
        print("Good job!")
       # clear_screen()
        return True  
    elif question != ans:
        return
        print("Naahh! Try again..")
             


def main():
    
    logo_page()
    scores()
    get_question_answers()
score = 0
main()    
