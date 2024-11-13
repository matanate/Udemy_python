resorces = {"Water": 300,
            "Milk": 200,
            "Coffee": 100,
            "Money": 0
            }

resorces_req = {"espresso": [50,0,18,1.5],
                "latte": [200,150,24,2.5],
                "cappuccino": [250,100,24,3]
                }

def report():
    global resorces
    print(f'''Water: {resorces["Water"]}ml  
Milk: {resorces["Milk"]}ml
Coffee: {resorces["Coffee"]}gr
Money: ${resorces["Money"]}''')

def check_resources(user_choice):
    global resorces
    if resorces_req[user_choice][0] > resorces["Water"]:
        print("Sorry there is not enough water.")
        return False
    if resorces_req[user_choice][1] > resorces["Milk"]:
        print("Sorry there is not enough milk.")
        return False
    if resorces_req[user_choice][2] > resorces["Coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True
def check_coins(user_choice, quarters, dimes, nickels, pennies):
    global resorces
    coins_value = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies
    if resorces_req[user_choice][3] > coins_value:
        print("Sorry that's not enough money. Money refunded. ")
        return False
    else:
        resorces["Money"] += resorces_req[user_choice][3]
        if coins_value > resorces_req[user_choice][3]:
            print(f"Here is ${coins_value - resorces_req[user_choice][3]:.2f} dollars in change.")
        return True

status_on = True
while status_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'report':
        report()
    elif user_choice == "espresso" or user_choice == "cappuccino" or user_choice == "latte":
        if check_resources(user_choice):
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            if check_coins(user_choice, quarters, dimes, nickels, pennies):
                resorces["Water"] -= resorces_req[user_choice][0]
                resorces["Milk"] -= resorces_req[user_choice][1]
                resorces["Coffee"] -= resorces_req[user_choice][2]
                print (f"Here is your {user_choice}. Enjoy!")
    elif user_choice == "off":
        status_on = False

        
