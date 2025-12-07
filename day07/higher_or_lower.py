import art
from game_data import data
import random



def get_random_data_item():
    index = random.randint(0, len(data))
    item = data[index]
    return item



def play_game():
    item_A = get_random_data_item()
    item_B = get_random_data_item()

    print(art.logo)

    player_score = 0

    correct = True

    while correct:

        print(f"Compare A: {item_A['name']}, a {item_A['description']}, from {item_A['country']}.")
        print(art.vs)
        print(f"Compare B: {item_B['name']}, a {item_B['description']}, from {item_B['country']}.")

        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if player_choice == "a" and item_A["follower_count"] > item_B["follower_count"]:
            player_score += 1
            print(f"That's right! Current score: {player_score}")
            item_B = get_random_data_item()

        elif player_choice == "b" and item_B["follower_count"] > item_A["follower_count"]:
            player_score += 1
            print(f"That's right! Current score: {player_score}")
            item_A = item_B
            item_B = get_random_data_item()

        else:
            print(f"Sorry, that's wrong. Final score: {player_score}")
            correct = False


play_game()