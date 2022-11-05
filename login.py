import gspread
from google.oauth2.service_account import Credentials


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


levels = ["Level 1", "Level 2", "Level 3"]

def get_user_name():
    """
    get player name
    """
    while True:    
        print("Enter game name to save game or get to the next level")
        print("Your name must be consist of letters only")
    
        player_name = input("Game name:")
   # print(f"game name: {player_name}")
    
        name_data = player_name
        if validate_name(name_data):
            print("Player name saved")
            break

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
def save_data_worksheet():
    """
    Update player information to worksheet
    """
    



name_data = get_user_name()


#def get_email():

#def get_level():