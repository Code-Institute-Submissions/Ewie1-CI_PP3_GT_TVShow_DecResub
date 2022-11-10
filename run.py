# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import sys
import os
from questionanswer_lev_one import questions
#from questionanswer_lev_one import answers
from questionanswer_lev_one import level_two
from questionanswer_lev_one import level_three
import login 



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
    print("There are 3 levels of tests\nScore 1000 points to get to the next level")
    input("Press any key to begin")
    clear_screen()
    logo_page()
    return True
    
    

def menu():
    """
    Give return player options to continue game
    """
    options = "1) About Game          2) Play Game\n"
    selected_option = input(options)
    print("" * 75)

    while selected_option not in ("1", "2"):
        print("You can only choose 1 or 2:")
        selected_option = input(options)
        
    if selected_option == "1":
        continue_play()
        
    elif selected_option == "2":
        clear_screen()
        logo_page()
        print("-" * 75)
        start_game()
        
    return selected_option     
     
def start_game():
    """
    Determine if palyer is new or Retruned
    """
    new_player = "1) I am a new player      2) Log me in\n"
    player_selection = input(new_player)

    while player_selection not in ("1", "2"):
        print("You can only choose 1 or 2:")
        player_selection = input(new_player)

    if player_selection == "1":
        play_game()
    
    elif player_selection == "2":
        login.validate_return_player()    

    return player_selection
         

def scores(score):
    """
    Use score count to determine game levels
    """
    if score == 1000:
        print("-" * 75)
        login.get_registered()
        get_level_two()
    elif score == 2000:
        get_level_three()
    elif score == 3000:
        print("You have won my game!\n Congratulations!")
    else:
        pass

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

def get_level_two():
    """
    Test function
    """
    print("level 2\n")
    print("-" * 75)
    while True:
        score = 1000

        for question in level_two:
            attempts = 3
        #    while attempts > 0:
            print(level_two[question]["question"])
            ans = input("Enter Show:")
            check = check_answer(question, ans, score, attempts)
            if check:
                score += 125
                scores(score)
                gameover(score)
           # attempts -= 1
        break

def get_level_three():
    """
    Test function
    """
    print("level 3\n")
    print("-" * 75)
    while True:
        score = 2000

        for question in level_three:
            attempts = 3
        #    while attempts > 0:
            print(level_three[question]["question"])
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
        print(f"Good job!{score + 125} \n")
        return True
    elif level_two[question]["answer"] == ans:
        print(f"Good job!{score + 125} \n")
        print("level 2")
        return True
    elif level_three[question]["answer"] == ans:
        print(f"Good job!{score + 125} \n")
        print("level 3")
        return True
    else:
        print("Naahh! Try again..")
        return False

def return_player_access():
    """
    Give access
    """


def continue_play():
    """
    Run function to contniue play
    """
   # clear_screen()
    logo_page()
   # scores()
   # get_question_answers()

def play_game():
    """"
    Start game
    """
    
    score = 0
    logo_page()
    scores(score)
    print("-" * 75)
    get_question_answers()
    gameover(score)
    

def main():
    """
    Main 
    """
    score = 0
    logo_page()
    intro()
    scores(score)
    menu()

   # get_question_answers()
    gameover(score)


main()
#start_game()
#get_level_two()
