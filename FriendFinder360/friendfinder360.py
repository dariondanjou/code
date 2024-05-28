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
#TODO create the logic for looping through all fake users' answers and comparing them to current users' answers
#TODO print results of the answer comparisons to the screen
#TODO create the 5 "fake" users and their answers in JSON format
#TODO read and print the 5 fake users info to terminal from the JSON file

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

USERS_DATA = {
    1000000000001: {
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
    1000000000002: {
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
    1000000000003: {
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
    1000000000004: {
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
    1000000000005: {
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
            "Ethical principles should never be compromised even at great personal loss": 3,
            "No Pain, No Gain": 4
        }
    }
}

def answer_questions(new_user_data):
    print("Answer the following questions:")
    if "answers" not in new_user_data:
        new_user_data["answers"] = {}
    for question in QUESTIONS:
        while True:
            try:
                print()
                print(question)
                answer = int(input(f"{VALID_ANSWER_MESSAGE}: "))
                if answer in VALID_ANSWERS:
                    new_user_data["answers"][question] = answer
                    break
                else:
                    print("Invalid answer. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
    return new_user_data

def main():
    users_data = USERS_DATA    
    
    print("Here is the current list of users: ")
    for user_id, user_info in users_data.items():
        if isinstance(user_info, dict):
            print(user_id)
            print(user_info.get('username'))
            print(user_info.get('First Name'))
            print(user_info.get('Last Name'))
            print() 

    # Generate a new user_id by getting the last key and adding 1
    new_user_id = max(users_data.keys()) + 1 if users_data else 1000000000001

    username = input("Enter username: ")
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name: ")

    # Create the new user's data
    new_user_data = {
        "username": username,
        "First Name": firstname,
        "Last Name": lastname,
        "answers": {}
    }

    #add new user to the dictionary
    users_data[new_user_id] = new_user_data

    #pass new user's data to answer_questions
    new_user_data = answer_questions(new_user_data)
    users_data[new_user_id] = new_user_data

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

if __name__ == '__main__':
    main()




    ###do this later### check if username is already in the users_data dictionary, if so pull up and print First and Last Name with a welcome back messsage


    #if username not in the dictionary, tell the user it's been created then prompt for First Name and Last Name, then go to asking questions


