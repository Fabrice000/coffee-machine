from ressources import MENU, ressources
#TODO-1: Une fonction qui gere le fonctionnement de la marchine
def marchine_controle():
    """This is the fuction who controle the user input if it's valid or not  """
    is_valid = True
    while is_valid:
        user_input = input("What would you like?(espresso/latte/cappuccino): ")
        if user_input == "off":
            is_valid = False
            return 0
        elif user_input == "report":
            is_valid = False
            return "report"
            
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            is_valid = False
            valid_user_input = user_input
            return valid_user_input
        else:
            print ("Invalid input")
            
# TODO-2: fonction qui sert en fonction du the choisir
def serve():
    """This is the main function who verify the coins proccess and serve the user """
    user_input_returned = marchine_controle()
    if user_input_returned == "espresso":
        is_runnig = True
        espresso  = (MENU["espresso"])
        espresso_ingre = espresso["ingredients"]
        
        if ressources["coffee"] < espresso_ingre["coffee"]:
            print("sorry there is not enough coffee")
        elif ressources["water"] < espresso_ingre["water"]:
            print("Sorry there is not enough water")
        else:
            user_coins = coins_input()
            if user_coins >= espresso["cost"]:
                ressources["water"] = ressources["water"] - espresso_ingre['water']
                ressources["coffee"] = ressources["coffee"] - espresso_ingre["coffee"]
                ressources["cost"] += espresso["cost"]
                change = round(user_coins - espresso["cost"], 2)
                print(f"Here is ${change} in change")
                print(f"Take your espresso, have enjoy!")
            
            else:
                print("Sorry your coins input is insufficient")
        return is_runnig
    elif user_input_returned == "latte" :
        is_runnig = True
        latte  = (MENU["latte"])
        latte_ingre = latte["ingredients"]
        if ressources["milk"] < latte_ingre["milk"]:
            print("sorry there are not enough milk")
        elif ressources["coffee"] < latte_ingre["coffee"]:
            print("sorry there is not enough coffee")
        elif ressources["water"] < latte_ingre["water"]:
            print("Sorry there is not enough water")
        else:
            user_coins = coins_input()
            if user_coins >= latte["cost"]:
            
                ressources["water"] = ressources["water"] - latte_ingre['water']
                ressources["milk"] = ressources["milk"] - latte_ingre['milk']
                ressources["coffee"] = ressources["coffee"] - latte_ingre["coffee"]
                ressources["cost"] += latte["cost"]
                change = round(user_coins - latte["cost"], 2)
                print(f"Here is ${change} in change")
                print(f"Take your latte, have enjoy!")
            else:
                print("Sorry your coins input is insufficient")
        return is_runnig
    elif user_input_returned == "cappuccino":
        is_runnig = True
        cappuccino  = (MENU["cappuccino"])
        cappuccino_ingre = cappuccino["ingredients"]
        if ressources["milk"] < cappuccino_ingre["milk"]:
            print("sorry there are not enough milk")
        elif ressources["coffee"] < cappuccino_ingre["coffee"]:
            print("sorry there is not enough coffee")
        elif ressources["water"] < cappuccino_ingre["water"]:
            print("Sorry there is not enough water")
        else:
            user_coins = coins_input()
            if user_coins >= cappuccino["cost"]:
                ressources["water"] = ressources["water"] - cappuccino_ingre['water']
                ressources["milk"] = ressources["milk"] - cappuccino_ingre['milk']
                ressources["coffee"] = ressources["coffee"] - cappuccino_ingre["coffee"]
                ressources["cost"] += cappuccino["cost"]
                change = round(user_coins - cappuccino["cost"], 2)
                print(f"Here is ${change} in change")
                print(f"Take your cappuccino, have enjoy!")
            else:
                print("Sorry your coins input is insufficient")
    elif user_input_returned == "report":
        is_runnig =  True
        for i in ressources:
            if i == "water" or i == "milk":
                print(f"{i}: {ressources[i]}ml")
            elif i == "coffee":
                print(f"{i}: {ressources[i]}g")
            else:
                print(f"{i}: ${ressources[i]}")
        return is_runnig
    else:
        print("Goodbye!")
        is_runnig =  False
    return is_runnig
        

# TODO-4: fonction qui calcul l'argent entrer dans la machine
def coins_input():
    """This is the function who calcalate the coins input by the user and check if it's sufficient"""
    print("PLease insert a coins")
    user_coins = float(input("How many quarter?:")) * 0.25
    user_coins += float(input("How many dimes?:")) * 0.1
    user_coins += float(input("How many nickles?:")) * 0.05
    user_coins += float(input("How many pennies?:")) * 0.01
        
    return user_coins



is_runnig = True
while is_runnig:
    is_runnig = serve()

