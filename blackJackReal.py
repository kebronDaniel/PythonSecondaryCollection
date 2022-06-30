import random


logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/ 
'''


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    if len(list_of_cards) == 2 and sum(list_of_cards) == 21:
        return 0

    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum(list_of_cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return 0
    elif user_score == 0:
        return 1
    elif dealer_score == 0:
        return 2
    elif user_score > 21:
        return 2
    elif dealer_score > 21:
        return 1
    elif user_score > dealer_score:
        return 1
    else:
        return 2


def play_game():

    user_cards = []
    dealer_cards = []

    for _ in range(2):
        user_cards.append(deal_cards())
        dealer_cards.append(deal_cards())

    end_game = False

    while not end_game:

        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards {user_cards} : Score = {user_score}")
        print(f"Dealer's first card {dealer_cards[0]}")

        if (user_score == 0 or dealer_score == 0) or (user_score > 21):
            end_game = True

        else:
            user_choice = input(
                "Do you want get another card? 'yes' or 'no':  ").lower()
            if user_choice == 'yes':
                user_cards.append(deal_cards())
            else:
                end_game = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_cards())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your cards : {user_cards} and your score {user_score}")
    print(f"Dealers cards : {dealer_cards} and your score {dealer_score}")
    return compare(user_score, dealer_score)


print(logo)
number_of_games = int(input("How many times do you want to play ? \n"))
user_points = 0
dealer_points = 0
for _ in range(number_of_games):
    print(f"--------------- Round {_ + 1} ---------------")
    value = play_game()
    if value == 1:
        user_points += 1
        print("You win")
        print(f"User points : {user_points}")
        print(f"Dealer points : {dealer_points}")
    elif value == 2:
        dealer_points += 1
        print("Dealer wins")
        print(f"User points : {user_points}")
        print(f"Dealer points : {dealer_points}")
    else:
        print("It's a Draw")
        print(f"User points : {user_points}")
        print(f"Dealer points : {dealer_points}")

if user_points > dealer_points:
    print("You are the Champion")
elif user_points < dealer_points:
    print("The Dealer is the Champion")
else:
    print("It's a Draw")
