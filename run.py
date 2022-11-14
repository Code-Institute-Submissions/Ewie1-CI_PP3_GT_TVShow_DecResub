# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import sys
import os
import time
from time import sleep
from colors import Color as Col
from questionanswer_lev_one import questions
from questionanswer_lev_one import level_two
from questionanswer_lev_one import level_three
import login




def logo_page():

    """
    print game logo and name
    """

    print(Col.YELLOW + "  __________________    ______________   ____________.__  "  )               
    print(Col.YELLOW + " /  _____\__    ___/    \__    ___\   \ /   /   _____|  |__   ______  _  __")
    print(Col.OKGREEN + "/   \  ___ |    |  ______ |    |   \   Y   /\_____  \|  |  \ /  _ \ \/ \/ /")
    print(Col.OKGREEN + "\    \_\  \|    | /_____/ |    |    \     / /        |   Y  (  <_> \     / ")
    print(Col.YELLOW + " \______  /|____|         |____|     \___/ /_______  |___|  /\____/ \/\_/  ")
    print(Col.YELLOW + "        \/                                         \/     \/               ")
    print(Col.OKGREEN + "-" * 75)
    print(Col.Green + "-" * 75)
    print("")


def intro():
    """
    Print game intro
    input any key to start game
    """
    time.sleep(0.5)
    print("Welcome to Guess That TV Shows!")
    time.sleep(1)
    print("Test your knowledge on some of the most famous TV show!")
    time.sleep(1)
    input(Col.Blue + "Press any key to begin")
    clear_screen()
    logo_page()
    return True
    
def menu():
    """
    Give return player options to continue game
    """
    time.sleep(0.5)
    print(Col.Blue + "Pick a choice from the Menu")
    time.sleep(0.5)
    options = "1. About Game          2. Play Game\n"
    selected_option = input(options)
    

    while selected_option not in ("1", "2"):
        print(Col.RED + "You can only choose 1 or 2:")
        selected_option = input(options)
        
    if selected_option == "1":
        clear_screen()
        logo_page()
        about_game()
        
    elif selected_option == "2":
        clear_screen()
        logo_page()
        start_game()
        
    return selected_option     

def about_game():
    """
    Decscribe how game is played 
    Return to intro page
    """
    print("Guess which show these top TV quotes are from?")
    print("One right answer gives you 125 point and no ponits for wrong answers")
    print("Your answers must be in lowercase")
    print("There are 3 levels of tests\nScore 1000 points to get to the next level")
    print("Each level may ask more questions ans it gets a bit trickier")
    print("After completing the first level yu can save your player info")
    print("Logging in will allow you to skip level 1 when you return to the game")
    input(Col.Blue + "Press any key to get back to the Home Screen")
    clear_screen()
    logo_page()
    menu()
    return True

def start_game():
    """
    Determine if palyer is new or Retruned
    """
    time.sleep(0.5)
    print(Col.Blue + "Are you new to this game?")
    time.sleep(0.5)
    new_player = "1) I am a new player      2) Log me in\n"
    player_selection = input(new_player)

    while player_selection not in ("1", "2"):
        print("You can only choose 1 or 2:")
        clear_screen()
        logo_page()
        time.sleep(1)
        player_selection = input(new_player)

    if player_selection == "1":
        clear_screen()
        play_game()
    
    elif player_selection == "2":
        login.validate_return_player()
        clear_screen()
        logo_page()
        return_player_access()    

    return player_selection

def return_player_access():
    """
    Give access
    """

    print(Col.Blue + "Choose Level")
    new_player = "Level 1       Level 2\n"
    player_selection = input(new_player)


    while player_selection not in ("1", "2"):
        print("You can only choose 1 or 2:")
        player_selection = input(new_player)

    if player_selection == "1":
        clear_screen()
        get_question_answers()
    
    elif player_selection == "2":
        clear_screen()
        logo_page()
        get_level_two()    

    return player_selection
    
def scores(score):
    """
    Use score count to determine game levels
    """
    for question in questions:
        if score == 1000:
            print(Col.Green + "Yaay!!! You cleared Level 1!")
            print(Col.Green + "Register and move on to the next Level")
            login.get_registered()
            clear_screen()
            get_level_two()
        elif score == 2000:
            print(Col.Green + "Yaay!!! You cleared Level 2!")
            time.sleep(1)
            get_level_three()
        elif score == 3000:
            print(Col.Green + "Yaay!!! You cleared Level 3!")
            time.sleep(1)
            print("You have won my game!\n Congratulations!")
        #elif score < 1000 or end_game():
            #print("Hello")
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
    print("Level 1\n")
    while True:
        score = 0

        for question in questions:
            attempts = 3
        #    while attempts > 0:
            print(questions[question]["question"])
            ans = input(Col.Green + "Enter Show:")
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
    print("Level 2\n")
    print(Col.Blue + "Guess which TV show the characters are from\n")
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
    print("Level 3\n")
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

           
def check_answer(question, ans, score, attempts):
    """
    Check player answer is wrong or correct, 
    print feed back 
    """  
    if questions[question]["answer"] == ans:
        print(Col.OKGREEN + f"Good job!{score + 125} \n")
        return True
    elif level_two[question]["answer"] == ans:
        print(Col.OKGREEN + f"Good job!{score + 125} \n")
        print("level 2")
        return True
    elif level_three[question]["answer"] == ans:
        print(Col.OKGREEN + f"Good job!{score + 125} \n")
        print("level 3")
        return True
    else:
        print(Col.FAIL + "Sorry wrong answer, Try again..")
        return False



def continue_play():
    """
    Run function to contniue play
    """
    logo_page()

def play_game():
    """"
    Start game
    """
    
    score = 0
    logo_page()
    scores(score)
    time.sleep(1)
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


def end_game():
    for question, i in enumerate(questions):
        
        quest = len(questions)
        print(quest[-1])
            
            
        
#end_game()

main()
#start_game()
#get_level_two()
