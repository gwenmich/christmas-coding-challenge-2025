import art
from menu import MENU


resources = {
    "water" : 300,
    "coffee": 100,
    "milk" : 200,
    "money" : 0
}


def check_ingredients(coffee_order):
    water = MENU[coffee_order]["ingredients"]["water"]
    coffee = MENU[coffee_order]["ingredients"]["coffee"]

    if coffee_order != "espresso":
        milk = MENU[coffee_order]["ingredients"]["milk"]
        if resources["milk"] < milk:
            return "Sorry there is not enough milk."

    if resources["water"] >= water and resources["coffee"] >= coffee:
        return True
    elif resources["water"] >= water:
        return "Sorry there is not enough coffee."
    elif resources["coffee"] >= coffee:
        return "Sorry there is not enough water."
    else:
        return "Sorry there are not enough ingredients."


def create_report():
    print(f"Water: {resources['water']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Milk: {resources['milk']}")
    print(f"Money: {resources['money']}")


def calculate_payment(q, d, n, p):
    return (q * 0.25) + (d * 0.1) + (n * 0.05) + (p * 0.01)


def remove_ingredients_amount_from_resources(coffee_type):
    if coffee_type != "espresso":
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]

    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    resources["money"] += MENU[coffee_type]["cost"]


def play_game():
    print(art.machine)

    working = True

    while working:

        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if coffee_choice == "report":
            create_report()

        elif coffee_choice == "off":
            print("Turning coffee machine off...")
            print("Goodbye.")
            working = False

        elif coffee_choice in MENU.keys():
            outcome = check_ingredients(coffee_choice)

            if outcome == True:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))

                total = calculate_payment(quarters, dimes, nickles, pennies)
                coffee_cost = MENU[coffee_choice]["cost"]

                if total >= coffee_cost:
                    remove_ingredients_amount_from_resources(coffee_choice)

                    change = total - coffee_cost

                    if change == 0:
                        print("Exact amount given. No change.")

                    print(f"Here is ${change} in change.")
                    print(f"Here is your {coffee_choice} ☕ Enjoy!")

                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(outcome)


play_game()