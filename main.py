from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

barista = CoffeeMaker()
menu = Menu()
payment = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        barista.report()
        payment.report()
    else:
        drink = menu.find_drink(choice)
        if barista.is_resource_sufficient(drink) and payment.make_payment(drink.cost):
            barista.make_coffee(drink)
