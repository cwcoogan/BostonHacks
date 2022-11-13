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
    empty = []
    preference = ({"like": {category}, "dislike":{category}})   
    if like == 1:
        if category in preference[1]:
            category.pop(1)
            empty.append(category) 
            preference['like'] = empty
    


     
    