
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
    print(Col.YELLOW + "  __________________    ______________   ____________.__  ")               
    print(Col.YELLOW + " /  _____\__    ___/    \__    ___\   \ /   /   _____|  |__   ______  _  __")
    print(Col.OKGREEN + "/   \  ___ |    |  ______ |    |   \   Y   /\_____  \|  |  \ /  _ \ \/ \/ /")
    print(Col.OKGREEN + "\    \_\  \|    | /_____/ |    |    \     / /        |   Y  (  <_> \     /")
    print(Col.YELLOW + " \______  /|____|         |____|     \___/ /_______  |___|  /\____/ \/\_/")
    print(Col.YELLOW + "        \/                                         \/     \/            ")
    print(Col.OKGREEN + "-" * 75)
    print(Col.Green + "-" * 75)
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
    print("Guess which TV shows these Quotes, Characters and Trevias are from?")
    print("There are 3 levels to this game")
    print("Score 1000 points to get to the next level")
    print("One right answer gives you 125 point and no ponits for wrong answers")
    print("Your answers must be in lowercase and the exact format of the TV show title")
    print("Each level have a different cateogory of questions and it gets a bit trickier")
    print("After completing the first level you can save your player info")
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
        print(Col.RED + "You can only choose 1 or 2:")
        player_selection = input(new_player)

    if player_selection == "1":
        clear_screen()
        logo_page()
        get_question_answers()
    
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
    print(Col.Blue + "Choose Level")
    new_player = "Level 1       Level 2\n"
    player_selection = input(new_player)

    while player_selection not in ("1", "2"):
        print(Col.RED + "You can only choose 1 or 2:")
        player_selection = input(new_player)

    if player_selection == "1":
        clear_screen()
        logo_page()
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
            print(Col.YELLOW + "Yaay!!! You cleared Level 1!")
            print(Col.YELLOW + "Register and move on to the next Level")
            login.get_registered()
            clear_screen()
            logo_page()
            get_level_two()
        elif score == 2000:
            print(Col.YELLOW + "Yaay!!! You cleared Level 2!")
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


def get_question_answers():
    """
    Run  game level one questions
    Determine score count
    """
    print("Level 1\n")
    while True:
        score = 0
        for question in questions:
            attempts = 3
            print(questions[question]["question"])
            ans = input(Col.Green + "Enter Show:")
            check = check_answer(question, ans, score, attempts)
            if check:
                score += 125
                scores(score)
        break


def get_level_two():
    """
    Run game level two questions
    Determine scores
    """
    print("Level 2\n")
    print(Col.Blue + "WHICH TV show are the CHARACTERS from?\n")
    while True:
        score = 1000
        for question in level_two:
            attempts = 3
            print(level_two[question]["question"])
            ans = input(Col.Green + "Enter Show:")
            check = check_answer(question, ans, score, attempts)
            if check:
                score += 125
                scores(score)
        break


def get_level_three():
    """
    Run game level three
    Determine score count
    """
    print("Level 3\n")
    while True:
        score = 2000
        for question in level_three:
            attempts = 3
            print(level_three[question]["question"])
            ans = input(Col.Green + "Enter Show:")
            check = check_answer(question, ans, score, attempts)
            if check:
                score += 125
                scores(score)
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
    

def main():
    """
    Main 
    """
    score = 0
    logo_page()
    intro()
    scores(score)
    menu()


main()


