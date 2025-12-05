import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_random_card():
    return random.choice(cards)

player = [get_random_card(), get_random_card()]
computer = [get_random_card(), get_random_card()]

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if play_game == "y":
    print(art.logo)
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {computer[0]}")
    next_or_pass = input("Type 'y' for another card, type 'n' to pass: ").lower()

    if next_or_pass == "n":
        print(f"Your final hand: {player}, final score: {sum(player)}")
        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
        if sum(computer) > sum(player):
            print("You lose")
            # play game loop
        elif sum(computer) == sum(player):
            print("It's a tie")
            # play game loop
        else:
            print("You win")
            #play game loop
    elif next_or_pass == "y":
        player.append(get_random_card())
        # print your cards and score
        # print computer first card
        # ask next or pass
        if sum(player) < 21:
            # another card or pass next_or_pass
            pass
        elif sum(player) == 21:
            print("Win! You have blackjack!")
            # play game loop
        else:
            print("You lose!")
            # play game loop