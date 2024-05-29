"""
Version 0.1 Basic Features:
- Enter your first name. 
- answer 10 questions. 
- don't persist memory. 
- compare to 5 pre-existing "fake" users. 
- show final ordered match ranking at the end
"""

#DONE design the data and logic structure in the form of comments here in the code page
#DONE create the 5 "fake" users and their answers in python dictionary
#DONE create the game flow of user entering their information and answering 10 questions, which get written to appropriate dictionary
#DONE print all the answers along with the usernames
#DONE create the logic for looping through all fake users' answers and comparing them to current users' answers
#DONE print results of the answer comparisons to the screen
#DONE if username not in the dictionary, tell the user it's been created then prompt for First Name and Last Name, then go to asking questions
#DONE check if username is already in the users_data dictionary, if so pull up and print First and Last Name with a welcome back messsage
#DONE read and print the 5 fake users info to terminal from the JSON file
#DONE after each match comparison update the users and their answers to the JSON file
    

"""
data structure is a single users_data data dictionary that gets written to and updated from JSON file to and from python dictionary
see users_data to reference data structure

list the 10 initial questions to be asked:
I tend to make decisions quickly and confidently
I believe that happiness is something that must be actively pursued and cultivated
I enjoy exploring new types of food and trying different cuisines
I find it difficult to remain calm and composed in stressful situations
It is irresponsible to bring children into today's world
I often rely on intuition rather than detailed analysis when making decisions
Personal growth requires constant effort and pushing beyond one's comfort zone
I'm more interested in maintaining routines than exploring new experiences
Ethical principles should never be compromised, even at great personal loss
No Pain, No Gain
"""

import random
import json
import os

VALID_ANSWERS = [1, 2, 3, 4]
VALID_ANSWER_MESSAGE = "STRONGLY DISAGREE [1] SOMEWHAT DISAGREE [2] SOMEWHAT AGREE [3] STRONGLY AGREE [4]"
QUESTIONS = [
    "I tend to make decisions quickly and confidently",
    "I believe that happiness is something that must be actively pursued and cultivated",
    "I enjoy exploring new types of food and trying different cuisines",
    "I find it difficult to remain calm and composed in stressful situations",
    "It is irresponsible to bring children into today's world",
    "I often rely on intuition rather than detailed analysis when making decisions",
    "Personal growth requires constant effort and pushing beyond one's comfort zone",
    "I'm more interested in maintaining routines than exploring new experiences",
    "Ethical principles should never be compromised, even at great personal loss",
    "No Pain, No Gain"
]

USERS_DATA_FILE = 'users_data.json'

# Read users_data from JSON file if it exists
if os.path.exists(USERS_DATA_FILE):
    with open(USERS_DATA_FILE, 'r') as file:
        users_data = json.load(file)
else:
    users_data = {
        100000000001: {
            "username": "alicewarren",
            "First Name": "Alice",
            "Last Name": "Warren",
            "answers": {
                "I tend to make decisions quickly and confidently": 3,
                "I believe that happiness is something that must be actively pursued and cultivated": 1,
                "I enjoy exploring new types of food and trying different cuisines": 4,
                "I find it difficult to remain calm and composed in stressful situations": 1,
                "It is irresponsible to bring children into today's world": 2,
                "I often rely on intuition rather than detailed analysis when making decisions": 3,
                "Personal growth requires constant effort and pushing beyond one's comfort zone": 1,
                "I'm more interested in maintaining routines than exploring new experiences": 2,
                "Ethical principles should never be compromised, even at great personal loss": 3,
                "No Pain, No Gain": 4
            }
        },
        100000000002: {
            "username": "jerrysmith",
            "First Name": "Jerry",
            "Last Name": "Smith",
            "answers": {
                "I tend to make decisions quickly and confidently": 4,
                "I believe that happiness is something that must be actively pursued and cultivated": 1,
                "I enjoy exploring new types of food and trying different cuisines": 3,
                "I find it difficult to remain calm and composed in stressful situations": 1,
                "It is irresponsible to bring children into today's world": 1,
                "I often rely on intuition rather than detailed analysis when making decisions": 3,
                "Personal growth requires constant effort and pushing beyond one's comfort zone": 2,
                "I'm more interested in maintaining routines than exploring new experiences": 2,
                "Ethical principles should never be compromised, even at great personal loss": 3,
                "No Pain, No Gain": 3
            }
        },
        100000000003: {
            "username": "agnesmbekeka",
            "First Name": "Agnes",
            "Last Name": "Mbekeka",
            "answers": {
                "I tend to make decisions quickly and confidently": 2,
                "I believe that happiness is something that must be actively pursued and cultivated": 2,
                "I enjoy exploring new types of food and trying different cuisines": 1,
                "I find it difficult to remain calm and composed in stressful situations": 1,
                "It is irresponsible to bring children into today's world": 2,
                "I often rely on intuition rather than detailed analysis when making decisions": 3,
                "Personal growth requires constant effort and pushing beyond one's comfort zone": 3,
                "I'm more interested in maintaining routines than exploring new experiences": 2,
                "Ethical principles should never be compromised, even at great personal loss": 3,
                "No Pain, No Gain": 1
            }
        },
        100000000004: {
            "username": "jamaljackson",
            "First Name": "Jamal",
            "Last Name": "Jackson",
            "answers": {
                "I tend to make decisions quickly and confidently": 3,
                "I believe that happiness is something that must be actively pursued and cultivated": 1,
                "I enjoy exploring new types of food and trying different cuisines": 4,
                "I find it difficult to remain calm and composed in stressful situations": 1,
                "It is irresponsible to bring children into today's world": 2,
                "I often rely on intuition rather than detailed analysis when making decisions": 3,
                "Personal growth requires constant effort and pushing beyond one's comfort zone": 1,
                "I'm more interested in maintaining routines than exploring new experiences": 2,
                "Ethical principles should never be compromised, even at great personal loss": 1,
                "No Pain, No Gain": 4
            }
        },
        100000000005: {
            "username": "joechristian",
            "First Name": "Joe",
            "Last Name": "Christian",
            "answers": {
                "I tend to make decisions quickly and confidently": 2,
                "I believe that happiness is something that must be actively pursued and cultivated": 1,
                "I enjoy exploring new types of food and trying different cuisines": 3,
                "I find it difficult to remain calm and composed in stressful situations": 4,
                "It is irresponsible to bring children into today's world": 2,
                "I often rely on intuition rather than detailed analysis when making decisions": 3,
                "Personal growth requires constant effort and pushing beyond one's comfort zone": 2,
                "I'm more interested in maintaining routines than exploring new experiences": 1,
                "Ethical principles should never be compromised, even at great personal loss": 3,
                "No Pain, No Gain": 4
            }
        }
    }

def calculate_match_percentage(current_user_answers, fake_users_data):
    match_percentages = {}

    for user_id, user_data in fake_users_data.items():
        total_difference = 0
        num_questions = len(current_user_answers)

        for question in current_user_answers:
            current_user_answer = current_user_answers[question]
            fake_user_answer = user_data['answers'][question]
            total_difference += abs(current_user_answer - fake_user_answer)

        # Maximum possible difference per question is 3 (4-1)
        max_possible_difference = num_questions * 3
        match_percentage = 100 - (total_difference / max_possible_difference * 100)
        match_percentages[user_id] = match_percentage

    return match_percentages

#get "First Name" by username
def get_first_name_by_username(users_data, username):
    for user_id, user_info in users_data.items():
        if user_info["username"] == username:
            return user_info["First Name"]
    return None

#get "Last Name" by username
def get_last_name_by_username(users_data, username):
    for user_id, user_info in users_data.items():
        if user_info["username"] == username:
            return user_info["Last Name"]
    return None

def main():
    #ask user for username
    username = input("Enter username: ")

    if username in [user["username"] for user in users_data.values()]:
        user_id = next(id for id, user in users_data.items() if user["username"] == username)
        print(f"Welcome back, {users_data[user_id]['First Name']}!")
        current_user_answers = users_data[user_id]['answers']
    else:
        print(f"Creating new user profile for {username}.")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")

        current_user_answers = {}
        for question in QUESTIONS:
            print()
            print(question)
            while True:
                try:
                    answer = int(input(f"{VALID_ANSWER_MESSAGE}: "))
                    if answer in VALID_ANSWERS:
                        current_user_answers[question] = answer
                        break
                    else:
                        print(f"Invalid input. Please enter one of the following: {VALID_ANSWERS}")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        #create new user entry
        new_user_id = max(map(int, users_data.keys())) + 1
        users_data[new_user_id] = {
            "username": username,
            "First Name": first_name,
            "Last Name": last_name,
            "answers": current_user_answers
        }

    #print updated users list
    print()
    print("Here is the updated list of users: ")
    for user_id, user_info in users_data.items():
        if isinstance(user_info, dict):
            print(user_id)
            print(user_info.get('username'))
            print(user_info.get('First Name'))
            print(user_info.get('Last Name'))
            print(list(user_info.get('answers').values())) #print just the digits of the answers
            print() 

    print("Well done! Now we will calculate closest matches...")
    print()

    #calculate match percentages
    match_percentages = calculate_match_percentage(current_user_answers, users_data)

    #sort match percentages from highest to lowest
    sorted_matches = sorted(match_percentages.items(), key=lambda item: item[1], reverse=True)

    #print match results
    firstname = get_first_name_by_username(users_data, username)
    lastname = get_last_name_by_username(users_data, username)
    print("Match percentages with other users for " + firstname, lastname + ": ")
    for user_id, match_percentage in sorted_matches:
        if users_data[user_id]["username"] != username:  #skip the current user
            print(f"{users_data[user_id]['First Name']} {users_data[user_id]['Last Name']}: {match_percentage:.2f}%")

    # Write updated users_data to JSON file
    with open(USERS_DATA_FILE, 'w') as file:
        json.dump(users_data, file, indent=4)

if __name__ == '__main__':
    main()






