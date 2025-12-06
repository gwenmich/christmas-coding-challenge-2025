import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and 11 in cards:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(p_score, c_score):
    if p_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose. Computer has Blackjack!"
    elif p_score == 0:
        return "You win with Blackjack!"
    elif p_score > 21:
        return "You lose"
    elif c_score > 21:
        return "Computer went over. You win"
    elif p_score > c_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(art.logo)
    player = [deal_card(), deal_card()]
    computer = [deal_card(), deal_card()]

    playing = True

    player_score = calculate_score(player)
    computer_score = calculate_score(computer)

    while playing:

        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {computer[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            playing = False
        else:
            next_choice = input("Type 'y' for another card, type 'n' to pass: ").lower()
            if next_choice == "y":
                player.append(deal_card())
            else:
                playing = False


    while computer_score != 0 and computer_score < 17:
        computer.append(computer)
        computer_score = calculate_score(computer)


    print(f"Your final hand: {player}, final score: {sum(player)}")
    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
    print(compare(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()