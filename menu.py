"""
    FUNCTION -- Menu()

    Parameter - Null

    Returns -- user_choice int value of like/dislike/super-like

    Notes -- We will need to alter this from L/D/S to the actual physical swipe value 
"""
preference = {}

def menu():
    user_choice = input("Welcome to Food Tinder:\nL: Like \nD: Dislike\n"
    "S: Super Like")   
    if user_choice.upper() == "L":
        return 1
    elif user_choice.upper() == "D":
        return 2
    elif user_choice.upper() == "S":
        return 3

def check_like(category, like):
    temp = [] # empty list to store item that will be removed from 
    super_list = [] # list to store value of super_Liked item
    
    preference = {"like": [category], "dislike":[category]} # dictionary to fill  
    if like == 1 and like not in  category: # if user selects LIKE & item is NOT in dict THEN append
        preference['like'] = like
    if like == 1 and like in category:
        pass # needs to Continue 
    if like == 2:
        preference.pop(preference[like])
        temp.append(category)
    if like == 3:
        super_list.append(like)
    
menu()
check_like('food', None)
    