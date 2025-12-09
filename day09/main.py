from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cafe_menu = Menu()
coffee_machine = CoffeeMaker()
till = MoneyMachine()

working = True

while working:

    coffee_choice = input(f"What would you like? ({cafe_menu.get_items()}): ")

    if coffee_choice == "off":
        print("Turning coffee machine off...")
        print("Goodbye!")
        working = False

    elif coffee_choice == "report":
        coffee_machine.report()
        till.report()

    else:
        drink = cafe_menu.find_drink(coffee_choice)
        if drink is not None:
            if coffee_machine.is_resource_sufficient(drink):
                if till.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
        else:
            print(drink)

