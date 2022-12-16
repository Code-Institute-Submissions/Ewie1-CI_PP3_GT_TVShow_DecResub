
import os
import time
from time import sleep
from colors import Color as Col
from questionanswer_lev_one import level_one
from questionanswer_lev_one import level_two
from questionanswer_lev_one import level_three
import login


def logo_page():
    """
    print game logo and name
    """

    print(Col.YELLOW + "    ___ _____     _____       __ _     ")              
    print(Col.YELLOW + "   / _ /__    \  /__   /\   // _| |__   _____      __")
    print(Col.OKGREEN + "  / /_\ / / /\_____ / /\\ \ / \ \| '_ \ / _ \ \ /\ / /")
    print(Col.OKGREEN + " / /_\\ /  / |_____ / /  \ V /_\ | | | | (_) \ V  V /")
    print(Col.YELLOW + " \____/ \/         \/    \_/ \__|_| |_|\___/ \_/\_/") 
    print(Col.OKGREEN + "-" * 60)
    print(Col.Green + "-" * 60)
    print("")                                               


def intro():
    """
    game intro
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
    Navigate to intructions
    Input option to play game
    """
    time.sleep(0.5)
    print(Col.Blue + "Pick a choice from the Menu")
    time.sleep(0.5)
    print(Col.Blue + "Enter numder 1 or 2 for you choice")
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
    print("Guess which TV shows names")
    print("There are 3 levels to this game")
    print("Level 1 Quotes") 
    print("Level 2 Characters")
    print("Level 3 Trivias")
    print("Score 1000 points to get to the next level")
    print("Answer right and score 125 points")
    print("Your answers must be in lowercase")
    print("And the exact format of the TV show title")
    print("After completing the first level you can save your player info")
    input(Col.Blue + "Press any key to get back to the Home Screen")
    clear_screen()
    logo_page()
    menu()
    return True


def start_game():
    """
    Determine if palyer is new or Retruned
    Give return player options to continue game
    Login
    """
    time.sleep(0.5)
    print(Col.Blue + "Are you new to this game?")
    time.sleep(0.5)
    print(Col.Blue + "Enter numder 1 or 2 for you choice")
    time.sleep(0.5)
    new_player = "1) I am a new player      2) Log me in\n"
    player_selection = input(new_player)

    while player_selection not in ("1", "2"):
        print(Col.RED + "You can only choose 1 or 2:")
        player_selection = input(new_player)

    if player_selection == "1":
        clear_screen()
        logo_page()
        get_level_one()
    
    elif player_selection == "2":
        clear_screen()
        logo_page()
        login.validate_return_player()
        clear_screen()
        logo_page()
        return_player_access()    

    return player_selection


def return_player_access():
    """
    Give access for level 1 and 2 to return player
    """
    time.sleep(0.5)
    print(Col.Blue + "Choose Level")
    time.sleep(0.5)
    print(Col.Blue + "Enter numder 1 or 2 for you choice")
    time.sleep(0.5)
    new_player = "Level 1       Level 2\n"
    player_selection = input(new_player)

    while player_selection not in ("1", "2"):
        print(Col.RED + "You can only choose 1 or 2:")
        player_selection = input(new_player)

    if player_selection == "1":
        clear_screen()
        logo_page()
        get_level_one_return()
    
    elif player_selection == "2":
        clear_screen()
        logo_page()
        get_level_two()    

    return player_selection
    

def scores(score):
    """
    Use score count to determine game levels
    """
    for question in level_one:
        if score == 1000:
            print(Col.YELLOW + "Yaay!!! You cleared Level 1!")
            print(Col.YELLOW + "Register and move on to the next Level")
            login.get_registered()
            clear_screen()
            logo_page()
            get_level_two()
        elif score == 2000:
            print(Col.YELLOW + "Yaay!!! You cleared this Level !")
            time.sleep(2)
            clear_screen()
            logo_page()
            get_level_three()
        elif score == 3000:
            print(Col.YELLOW + "Yaay!!! You cleared Level 3!")
            time.sleep(1)
            print("You have won my game!\n Congratulations!")
        else:    
            pass


def clear_screen():
    """
    Clear screen
    """
    os.system('clear') 


def get_level_one():
    """
    Run  game level one questions
    Determine score count
    """
    print("Level 1\n")
    print(Col.Blue + "Quotes!  Guess the show\n")
    while True:
        score = 0
        for question in level_one:
            attempts = 3
            while attempts > 0:
                print(level_one[question]["question"])
                ans = input(Col.Green + "Enter Show:")
                check = check_answer(question, ans, attempts, score)
                if check:
                    score += 125
                    scores(score)
                    break
                attempts -= 1
                if attempts == 0 and ans == "":
                    restart_level_one()    
        break
    restart_level_one()


def get_level_one_return():
    """
    Run  game level one questions
    Determine score count
    """
    print("Level 1\n")
    print(Col.Blue + "Quotes!  Guess the show\n")
    while True:
        score = 1000
        for question in level_one:
            attempts = 3
            while attempts > 0:
                print(level_one[question]["question"])
                ans = input(Col.Green + "Enter Show:")
                check = check_answer(question, ans, attempts, score)
                if check:
                    score += 125
                    scores(score)
                    break
                attempts -= 1
                if attempts == 0 and ans == "":
                    restart_level_one_return()
   
        break
    restart_level_one_return()


def get_level_two():
    """
    Run game level two questions
    Determine scores
    """
    print("Level 2\n")
    print(Col.Blue + "Characters!   Guess the show\n")

    while True:
        score = 1000
        for question in level_two:
            attempts = 3
            while attempts > 0:
                print(level_two[question]["question"])
                ans = input(Col.Green + "Enter Show:")
                check = check_answer(question, ans, attempts, score)
                if check:
                    score += 125
                    scores(score)
                    break
                attempts -= 1
                if attempts == 0 and ans == "":
                    restart_level_two()  
        break
    restart_level_two()


def get_level_three():
    """
    Run game level three
    Determine score count
    """
    print("Level 3\n")
    print(Col.Blue + "Trivias!\n")
    while True:
        score = 2000
        for question in level_three:
            attempts = 3
            while attempts > 0:
                print(level_three[question]["question"])
                ans = input(Col.Green + "Enter Show:")
                check = check_answer(question, ans, attempts, score)
                if check:
                    score += 125
                    scores(score)
                    break
                    attempts -= 1
                    if attempts == 0 and ans == "":
                        restart_level_three()  
        break
    restart_level_three()


def check_answer(question, ans, attempts, score):
    """
    Check player answer is wrong or correct, 
    print feed back 
    """
    if level_one[question]["answer"] == ans:
        print(Col.OKGREEN + f"Good job! {score + 125}points! \n")
        return True
    elif level_two[question]["answer"] == ans:
        print(Col.OKGREEN + f"Good job! {score + 125}points! \n")
        return True
    elif level_three[question]["answer"] == ans:
        print(Col.OKGREEN + f"Good job! {score + 125}points! \n")
        return True
    elif ans == "":
        print(Col.FAIL + "Invalid Input: You give no answer...")
        print(Col.FAIL + f"You MUST give an answer \nYou have {attempts - 1} attempts left :(") 
        return    
    else:    
        print(Col.YELLOW + f"Wrong Answer :( \nYou have {attempts - 1} left! \n 0 point :(")
        return False
        

def restart_level_one():
    """
    Restart level
    Reset game
    """
    print(Col.YELLOW + "Enter 3 to Restart Level")
    print(Col.YELLOW + "Enter 4 to Exit to Main Menu")
    player_selection = input()

    while player_selection not in ("3", "4"):
        print(Col.RED + "You can only choose 3 or 4:")
        player_selection = input()

    if player_selection == "3":
        clear_screen()
        logo_page()
        get_level_one()
    elif player_selection == "4":
        clear_screen()
        main()
    
    return player_selection 


def restart_level_one_return():
    """
    Restart level for return player
    Reset game
    """
    print(Col.YELLOW + "Enter 3 to Restart Level")
    print(Col.YELLOW + "Enter 4 to Exit to Main Menu")
    player_selection = input()

    while player_selection not in ("3", "4"):
        print(Col.RED + "You can only choose 3 or 4:")
        player_selection = input()

    if player_selection == "3":
        clear_screen()
        logo_page()
        get_level_one_return()
    elif player_selection == "4":
        clear_screen()
        main()
    
    return player_selection


def restart_level_two():
    """
    Restart level
    Reset game
    """
    print(Col.YELLOW + "Enter 3 to Restart Level")
    print(Col.YELLOW + "Enter 4 to Exit to Main Menu")
    player_selection = input()

    while player_selection not in ("3", "4"):
        print(Col.RED + "You can only choose 3 or 4:")
        player_selection = input()

    if player_selection == "3":
        clear_screen()
        logo_page()
        get_level_two()
    elif player_selection == "4":
        clear_screen()
        main()
    
    return player_selection  


def restart_level_three():
    """
    Restart level
    Reset game
    """
    print(Col.YELLOW + "Enter 3 to Restart Level")
    print(Col.YELLOW + "Enter 4 to Exit to Main Menu")
    player_selection = input()

    while player_selection not in ("3", "4"):
        print(Col.RED + "You can only choose 3 or 4:")
        player_selection = input()

    if player_selection == "3":
        clear_screen()
        logo_page()
        get_level_three()
    elif player_selection == "4":
        clear_screen()
        main()
    
    return player_selection                 


def main():
    """
    Main 
    Call game functions
    """
    score = 0
    logo_page()
    intro()
    scores(score)
    menu()


main()