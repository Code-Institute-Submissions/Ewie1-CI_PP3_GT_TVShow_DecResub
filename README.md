# Gess That TVshow
(Developer: Ewart Hestick)

![Mockup image]()

[Live webpage](https://guess-that-tvshow2.herokuapp.com/)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
3. [Design](#design)
    1. [Structure](#structure)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
    3. [Python Libraries](#python-libraries)
    4. [Third Party Libraries](#third-party-libraries)
5. [Features](#features)
    1. [Intro](#intro)
    2. [Menu](#menu)
    3. [Game Instructions](#game-instructions)
    4. [Play Options](#play-options)
    5. [Log-in](#log-in)
    6. [Sign-up](#sign-up)
    7. [User Greetings](#users-greetings)
    8. [Game](#game)
    9. [Game Levels](#game-levels)
    10. [End Game](#end-game)
    11. [User Input Validation](#user-input-validation)
6. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [Accessibility](#accessibility)
    4. [Performance](#performance)
    5. [Device testing](#performing-tests-on-various-devices)
    6. [Browser compatibility](#browser-compatability)
    7. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals 

### User Goals

- Play a fun quiz game
- Get high scores and high levels
- Be able to log a game name
- Return and login with access to higher levels

### Site Owner Goals

- Create a quiz game that is fun and responsive
- Have user be able to create a profile
- Have a response to every user input in the game
- Ensure the user know how the game is played

## User Experience

### Target Audience

- All audience
- Recommened 10yrs and older


### User Stories

#### First-time User 
1. I want to feel welcome
2. I want to have option to view game instructions
3. I want to have the option to have a player name and save a profile
4. I want to know when i make a wrong input
5. I want to know my scores

#### Returning User
 
 5. I want the game to remeber me
 6. I want to have an easy login option
 7. I want to have access to different levels
 8. I want to 
 9. I want to "add level column to access levels"


#### Site Owner 

10. As a owner I want the users to have navigation options 
11. As a owner I want user get feed back if input is wrong
12. As a site owner I want users info to be save and accessed in a Google Spread Sheet
13. I want user to play game at different levels

## Design

### Structure
This website was structured with the gym logo which give a gym it character but also with the regular easy to use nav bar, a body of information and the regular footer which give the final characteristics of a funtional webpage. The wedsite has three pages:

- Home 
- About page
- Become a member page

## Technologies Used

### Languages

- Python

### Frameworks & Tools
- Git
- GitHub
- Gitpod
- Google Cloud
- Google Sheets
- Heroku
- PEP8
- VSCode

### Python Libraries

- os
- time
- sleep
- sys

### Third Party Libraries

- colorama
- email_validator
- gspread
- google.oauth2.service_account

## Features

### Intro 
- Colorful logo
- Welcome message
- Option to begin
### Menu
- Gives option to see game instructions
- Raise error if options input values are not to the required format
- Give option to play game
### Game Instructions
- Instruction on how game is played
- Option to return to menu
### Play Options
- Play game as a new player
- Raise error if options input values are not to the required format
- Login as a return player
### Log-in
- Enter your saved game info
- Validates user input values
- Raise error in info does not exist
- Option to choose game level to play
### Sign-up
- After completing Level 1, create a game profile
- Validates user input values
- Save name, email and level to a google spread sheet
### Users Greetings
- Give welcome back message to return user
### Game
- Print one out of eight question one after the other
- Give feedback for input answer 
- Show score for answers
- Complete level 1 and create your profile
- Score 1000 points to get to different levels
### Game Levels
- Three game levels
### End Game
### User Input Validation
- Raise error if name input values are not to the required format
- Raise error if email input values are not to the required format
- Raise error if level input values are not to the required format
- Raise error if return user input info does not exist
- Raise error if options input values are not to the required format

## Validation
- 


### Testing user stories

1. I want to feel welcome

   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Color contrast | Bright color contrast and images with laughter |Website feels like the gym  | Works as expected |

   <details><summary>Screenshots</summary>
   <img src="">
   </details>

2.  I want to have option to view game instructions

    | **Feature** | **Action** | **Expected Result** | **Actual Result** |
    |-------------|------------|---------------------|-------------------|
    | Map | Scroll down on first page and click the google mag  | Goolge show gym location in the city | Works as expected |

     <details><summary>Screenshots</summary>
     <img src="">
     </details>

3. I want to have the option to have a player name and save a profile
   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Gym interior image | Scroll down on home page | Find pictures of the gym interior | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="">
    </details>

4. I want to know when i make a wrong input

   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Trian with us and Gym comforts list | Scroll down on home page  | Readable intriguing list | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="">
    </details>

5. I want the game to remeber me
   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Signup From | Cick signup button,Nav bar | Directed to signup page | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="">
    </details>

6. I want to have an easy login option   
   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Footer  on all pages | On any page scroll to the footer | See phone number and email address | Works as expected |

     <details><summary>Screenshots</summary>
     <img src="">
     </details>

7. I want to have access to different levels

   | **Feature** | **Action** | **Expected Result** | **Actual Result** |   
   |-------------|------------|---------------------|-------------------|
   | About Us pragraph | Navigate to the us page in menu bar  | Read  | Works as expected |

     <details><summary>Screenshots</summary>
     <img src="">
     <img src="">
     </details>

8. 

   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Membership Cards | Navigate to the About Uspage Scrooll down | Read | Works as expectd |

     <details><summary>Screenshots</summary>
     <img src="">
     <img src="">
     </details>

9. 

   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Footer - social media section | On any page scroll to the bottom | Click on social media links | Works as expected | 

     <details><summary>Screenshots</summary>
     <img src="">
     </details>


10. As a owner I want the users to have navigation options 

    | **Feature** | **Action** | **Expected Result** | **Actual Result** |
    |-------------|------------|---------------------|-------------------|
    | Signup Form | U Navigate sign up page click dropdown option| Choose from drop down option | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="">
    <img src="">
    </details>

11. As a owner I want user get feed back if input is wrong

    | **Feature** | **Action** | **Expected Result** | **Actual Result** |
    |-------------|------------|---------------------|-------------------|
    | 404 error page | On non-matched URL| Choose from drop down option | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="">
    </details>

12. As a site owner I want users info to be save and accessed in a Google Spread Sheet

    | **Feature** | **Action** | **Expected Result** | **Actual Result** |
    |-------------|------------|---------------------|-------------------|
    | Signup form | Navigate to signup page | Leave comments | Works as expected |

     <details><summary>Screenshots</summary>
     <img src="">
     <img src="">
     </details>
    
## Bugs
## Deployment
### Heroku
This application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name (this project is named "ci-pp3-connect4") and choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars store any sensitive data you saved in .json file. Name 'Key' field, copy the .json file and paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, I set up 'Python' and 'node.js' in that order.
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To link up our Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below
9.  Choose the branch you want to buid your app from
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

## Credits
## Aknowledgements