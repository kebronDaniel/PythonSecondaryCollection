from cmath import e
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackJack():
    dealers_cards = random.choices(deck, k=2)
    users_cards = random.choices(deck, k=2)

    print(f"Your cards : {users_cards}")
    print(f"Computer's First card : {dealers_cards}")

    def user_wins(users_cards, dealers_cards):
        users_score = sum(users_cards)
        dealers_score = sum(dealers_cards)

        if users_score > 21:
            return False
        else:
            if users_score > dealers_score or dealers_score > 21:
                return True

    def check_draw(users_cards, dealers_cards):
        users_score = sum(users_cards)
        dealers_score = sum(dealers_cards)
        if users_score == dealers_score:
            return True
        else:
            return False

    def end_game():
        if user_wins(users_cards, dealers_cards):
            print("You win")
            print(f"Your cards {users_cards}")
            print(f"dealers cards {dealers_cards}")
            return True
        elif check_draw(users_cards, dealers_cards):
            print("It's a draw")
            print(f"Your cards {users_cards}")
            print(f"dealers cards {dealers_cards}")
            return True
        else:
            print("dealer wins")
            print(f"Your cards {users_cards}")
            print(f"dealers cards {dealers_cards}")
            return True

    def add_card():
        users_cards.append(random.choice(deck))
        if sum(dealers_cards) < 17:
            dealers_cards.append(random.choice(deck))

    can_play = True
    while can_play:
        user_choice = input(
            "Do you want another card ? 'yes' or 'no' : ").lower()
        if user_choice == 'yes':
            add_card()
            if end_game():
                can_play = False
        elif user_choice == 'no':
            if end_game():
                can_play = False

        else:
            print("Invalid input")


blackJack()
