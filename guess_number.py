
import random

logo = ''''
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  \__   __/|\     /|(  ____ \  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/     ) (   | )   ( || (    \/  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____      | |   | (___) || (__      |   \ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )     | |   |  ___  ||  __)     | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |     | |   | (   ) || (        | | \   || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |     | |   | )   ( || (____/\  | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)     )_(   |/     \|(_______/  |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/
'''


def checker(num1, num2):
    if num1 == num2:
        return 0
    elif num1 > num2:
        return 1
    else:
        return 2


def play():
    selected_number = random.randint(1, 100)
    print(logo)

    level = input("Select a difficulty level: 'easy' or 'hard' : ").lower()
    if level == 'easy':
        chances = 10
    else:
        chances = 5

    for _ in range(chances):
        print(f"You have {chances} chances to Go")
        user_guess = int(input("Guess the number : "))
        result = checker(num1=user_guess, num2=selected_number)
        if result == 0:
            print(f"You have got the number, The number was {selected_number}")
            break
        elif result == 1:
            print("Too high")
            chances -= 1
        else:
            print("Too low")
            chances -= 1
    else:
        print("Game Over")
        print(f"The number was {selected_number}")


play()
