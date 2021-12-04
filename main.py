from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


"""Create Objects from the above classes to begin using them."""
my_menu = Menu()
my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)




