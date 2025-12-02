import art

print(art.logo)

bidding = True
bidders = {}

def find_highest_bidder(bidding_info):
    highest_bid = 0
    highest_bidder = ""
    for bidder, bid in bidders.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder

    print(f"The winner is {highest_bidder.capitalize()} with a bid of £{highest_bid}.")


while bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: £"))
    bidders[name] = bid

    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if next_bidder == "yes":
        print("\n" * 50)
    else:
        bidding = False
        find_highest_bidder(bidders)




