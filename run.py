# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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

def logo_page():

    """
    print game logo and name
    """

    print( "  __________________    ______________   ____________.__  "  )               
    print(" /  _____\__    ___/    \__    ___\   \ /   /   _____|  |__   ______  _  __")
    print("/   \  ___ |    |  ______ |    |   \   Y   /\_____  \|  |  \ /  _ \ \/ \/ /")
    print("\    \_\  \|    | /_____/ |    |    \     / /        |   Y  (  <_> \     / ")
    print(" \______  /|____|         |____|     \___/ /_______  |___|  /\____/ \/\_/  ")
    print("        \/                                         \/     \/               \n")
    print("                      Can you Guess That TV Show \n")


logo_page()