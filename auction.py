import os

auction = []


def add_auction():
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    auction.append({"name": name, "bid": bid})

    prompt_other = input(
        "Is there another bidder? Type 'yes' or 'no'\n").lower()
    if prompt_other == 'yes':
        os.system('clear')
        add_auction()
    else:
        bid_collector = []
        for person in auction:
            bid_collector.append(person["bid"])
        winner = auction[bid_collector.index(max(bid_collector))]
        print(
            f"The winner is {winner['name']} and the amount is {winner['bid']}$")


add_auction()
