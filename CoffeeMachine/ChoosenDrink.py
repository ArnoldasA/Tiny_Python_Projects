from Data import MENU
from Money import transaction
from Report import report
from Data import resources


# TODO OFF is the keyword for the coffee machine to stop


def drink_selection():
    turn_off = False

    while not turn_off:
        report("report")
        choice = input("What would you like? (espresso/latte/cappuccino)")
        report(choice)
        user_selection = choice
        supply_water = resources["water"]
        supply_milk = resources["milk"]
        supply_coffee = resources["coffee"]

        for items in MENU:
            if user_selection == items:
                water_cost = MENU[items]['ingredients']['water']
                if user_selection != "espresso":
                    milk_cost = MENU[items]["ingredients"]['milk']
                coffee_cost = MENU[items]["ingredients"]['coffee']
                cost = MENU[items]['cost']
                if supply_water < water_cost or supply_coffee < coffee_cost or supply_milk < milk_cost:
                    print("You have a supply shortage, Try a different drink or turn the machine off")
                    print(f"Water held:{supply_water} Water needed:{water_cost}\nCoffee held:{supply_coffee} Coffee "
                          f"needed:{coffee_cost}\nMilk held:{supply_milk} Milk needed:{milk_cost}")
                else:
                    print(f"The cost of the drink is {cost}")
                    transaction(cost)
                    print(f"Enjoy your {user_selection}")

                    if user_selection != "espresso":
                        resources["water"] -= water_cost
                        resources["coffee"] -= coffee_cost
                        resources["money"] += cost
                    else:
                        resources["water"] -= water_cost
                        resources["milk"] -= milk_cost
                        resources["coffee"] -= coffee_cost
                        resources["money"] += cost
        if choice == "off":
            turn_off = True
            return turn_off
