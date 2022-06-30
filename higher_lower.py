
import random

data = [

    {
        "name": "Messi",
        "follower_count": 281,
        "description": "A Footballer",
        "Country": "Argentina"
    },
    {
        "name": "C.Ronaldo",
        "follower_count": 366,
        "description": "A Footballer",
        "Country": "Portugal"
    },
    {
        "name": "Helen",
        "follower_count": 121,
        "description": "A Tv Host",
        "Country": "U.S"
    },
    {
        "name": "Bob Marly",
        "follower_count": 100,
        "description": "A Musician",
        "Country": "Jamica"
    },
    {
        "name": "Bill Gates",
        "follower_count": 132,
        "description": "A Programmer",
        "Country": "U.S"
    },
    {
        "name": "Miley Cyrus",
        "follower_count": 151,
        "description": "A Musician",
        "Country": "U.S"
    },
    {
        "name": "Virat kohli",
        "follower_count": 166,
        "description": "A Cricket player",
        "Country": "India"
    },
    {
        "name": "Messi",
        "follower_count": 500,
        "description": "A Footballer",
        "Country": "Argentina"
    },
    {
        "name": "Neymar",
        "follower_count": 164,
        "description": "A Footballer",
        "Country": "Brazil"
    },
    {
        "name": "Justin Bieber",
        "follower_count": 363,
        "description": "A Musician",
        "Country": "Canada"
    },
    {
        "name": "Dwayne",
        "follower_count": 278,
        "description": "An Actor",
        "Country": "U.S"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 281,
        "description": "A Social media star",
        "Country": "U.S"
    },
    {
        "name": "Katy perry",
        "follower_count": 182,
        "description": "A Musician",
        "Country": "U.S"
    }
]

logo = '''
  _     _       _               
 | |__ (_) __ _| |__   ___ _ __ 
 | '_ \| |/ _` | '_ \ / _ \ '__|
 | | | | | (_| | | | |  __/ |   
 |_| |_|_|\__, |_| |_|\___|_|   
 | | _____|___/ _____ _ __      
 | |/ _ \ \ /\ / / _ \ '__|     
 | | (_) \ V  V /  __/ |        
 |_|\___/ \_/\_/ \___|_|        
                                                 
'''

vs = '''
 __   _____ 
 \ \ / / __|
  \ V /\__ \\
   \_/ |___/
           
'''


def compare(person1, person2):
    if person1["follower_count"] > person2["follower_count"]:
        return 1
    else:
        return 2


def pick_person():
    return data[random.randint(1, len(data) - 1)]


def are_same(person1, person2):
    if person1["name"] == person2["name"]:
        return True
    else:
        return False


def play():

    print(logo)

    person1 = pick_person()
    person2 = pick_person()

    end_game = False
    score = 0
    while not end_game:
        person2 = pick_person()

        if not are_same(person1, person2):
            print(
                f"Compare A: {person1['name']}, {person1['description']} from {person1['Country']}")
            print(vs)
            print(
                f"Compare B: {person2['name']}, {person2['description']} from {person2['Country']}")

            user_guess = input("Who has more Followers? 'A' or 'B' : ")

            users_person = {}
            computers_person = {}

            if user_guess == "A":
                users_person = person1
                computers_person = person2
            elif user_guess == "B":
                users_person = person2
                computers_person = person1
            else:
                print("you typed the wrong character")
                break

            value = compare(users_person, computers_person)
            if value == 1:
                score += 1
                print(f"You are right, current score is {score}")
                users_person = person1
            else:
                print(f"You are wrong , your current score is {score}")
                break

        else:
            continue


play()
