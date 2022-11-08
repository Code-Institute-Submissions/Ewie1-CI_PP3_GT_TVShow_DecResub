# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import sys
import os
from questionanswer_lev_one import questions
from questionanswer_lev_one import answers



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


def intro():
    """
    Print game intro
    input any key to start game
    """
    print("Welcome to Guess That TV Shows!")
    print("Test your knowledge on some of the most famous TV show!")
    print("Guess which show these top TV quotes are from?")
    print("There are 3 levels of tests\nScore 1000 ponits to get to the next level")
    input("Press any key to begin")
    clear_screen()
    logo_page()
    return True




def scores(score):
    """
    Use score count to determine game levels
    """

    if score >= 1000:
        print("Run level 1")
        continue_play()
         
        return True
    elif score >= 1000:
        print("Run level 2")
    elif score >= 2000:
        print("Run level 3")
    elif score == 3000:
        print("End/Restart game")
    else:
        print("end game")

def gameover(score):
    """
    """
        
    if score > 875 and score < 1000:
        print("Gameover")
        print("Try again")
    elif len(questions) and score == 1900: 
        print("Gameover")
    elif len(questions) and score == 2900:
        print("gameover")
    else:
        pass       
    

def clear_screen():
    """
    Clear screen
    """
    os.system('clear') 

def get_question_answers():
    """
    Test function
    """
    while True:
        score = 0

        for question in questions:
            attempts = 3
        #    while attempts > 0:
            print(questions[question]["question"])
            ans = input("Enter Show:")
            check = check_answer(question, ans, score, attempts)
            if check:
                score += 125
                scores(score)
                gameover(score)
           # attempts -= 1
        break

# def get_question_answers():

 #   """
 #   get questions and answers and print for player input
 #   loop our attepmt variables
 #   """
 #   print("                      Can you Guess The TV Show?? \n")
  #  score = 0
 #   for question in questions:
  #      attempts = 3 
  #  while attempts > 0:
 #       randoms = random.choice([question for question in questions.values()])
 #       question = randoms["question"]
 #       print(question)
 #       question = randoms["answer"]
 #       print("")
 #       ans = input("Guess the Show:")
 #       check = check_answer(question, ans, score, attempts)
  #      if check:
  #          score += 125
           # continue_play()
  #          break
  #      attempts -= 1
           
              
def check_answer(question, ans, score, attempts):
    """
    Check player answer is wrong or correct, 
    print feed back 
    """  
    if questions[question]["answer"] == ans:
        print(f"Good job!{score + 125} ")
        
        return True
    else:
        print("Naahh! Try again..")
        return False

def continue_play():
    """
    Run function to contniue play
    """
   # clear_screen()
    logo_page()
   # scores()
   # get_question_answers()

def main():
    """
    Main 
    """
    score = 0
    logo_page()
    intro()
    scores(score)
    get_question_answers()
    gameover(score)


main()
  
