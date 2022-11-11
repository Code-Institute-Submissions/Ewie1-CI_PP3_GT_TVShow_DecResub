import gspread
from google.oauth2.service_account import Credentials
#from email_validator import validate_email, EmailNotValidError


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

LOGIN = Credentials.from_service_account_file("login.json")
SCOPED_LOGIN = LOGIN.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_LOGIN)
SHEET = GSPREAD_CLIENT.open("login")



def get_user_name():
    """
    get player name
    """
    while True:    
        print("Enter game name to save game or get to the next level")
        print("Your name must be consist of letters only")
    
        player_name = input("Game name:")
        name_data = player_name
        if validate_name(name_data):
            print("Thankyou")
            break
    return name_data

def get_user_email():
    """
    get player email
    """
    while True:    
        print("Enter your email to save game or get to the next level")
        print("Your name must be consist of letters only")
    
        player_email = input("Enter your email:")    
        email_data = player_email
        if val_email(email_data):
            print("Thankyou")
            break
    return email_data

def get_user_level():
    """
    get player level
    """
    while True:    
        print("Enter game level to save game or get to the next level")
        print("Your name must be consist of letters only")
    
        player_level = input("Game level:")
        level_data = player_level
        if validate_level(level_data):
            print("Thankyou")
            break
    return level_data

def validate_name(name):
    """
    Validate player name
    """
    try:
        if len(name) != 5:
            raise ValueError(f"Your name must be consisted of 5 digits, you provided {len(name)}")
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.\n")
        return False
    return True

def val_email(email):
    """
    Validate player name
    """
    try:
        validate_email(email)
        return True    
    except EmailNotValidError as e:
        print(f"Invalid data: {e}, Please try again.\n")
        return False
    return True

def validate_level(level):
    """
    Validate player name
    """
    try:
        if len(level) != 5:
            raise ValueError(f"Your name must be consisted of 5 digits, you provided {len(level)}")
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.\n")
        return False
    return True


def save_data_worksheet(data):
    """
    Update player information to worksheet
    """
    print("Saving name...")
    name_save = SHEET.worksheet("player")
    name_save.append_row(data)
    print("Player saved")

def get_registered():
    """
    Store all user input in a list and
    add to spreadsheet
    """
    data = []
    n = get_user_name()
    e = get_user_email()
    l = get_user_level()

    data.append(n)
    data.append(e)
    data.append(l)
    new_data = [val for val in data]
    save_data_worksheet(new_data)

def validate_return_player():
    """
    Get player info, validate 
    """    
    
    info = []
    n = get_user_name()
    e = get_user_email()
    l = get_user_level()

    info.append(n)
    info.append(e)
    info.append(l)

    player_data = SHEET.worksheet("player").get_all_values()

    if info in player_data:
        print(f"Wecome back {n}!")
    else:
        print("Your login infermation does not match")
        print("Please check your player name and email")
        print("Try again")
        validate_return_player()

#def main():
    #user_info_list(n, e, l)
   # get_user_name()
   # get_user_email()
   # get_user_level()
   # validate_name(name)
   # validate_email(email)
   # validate_level(level)

    #save_data_worksheet(data)
    #user_info_list(n, e, l)
#get_player_info(n, e, l)
