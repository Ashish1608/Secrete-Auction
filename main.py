from art import logo
import os
def clear(): return os.system('cls')


def find_winner(bidder_list):
    winner = ''
    highest_price = 0

    for bidder in bidder_list:
        if bidder_list[bidder] > highest_price:
            highest_price = bidder_list[bidder]
            winner = bidder

    return f"The winner is {winner} with a bid of ${highest_price}"


print(logo)

bidders = {}

should_continue = True

while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    is_another_bidder = input(
        "\nAre there any other bidders? Type 'yes or 'no'.\n").lower()

    if is_another_bidder == 'yes':
        clear()
    elif is_another_bidder == 'no':
        should_continue = False
        print(find_winner(bidders))
