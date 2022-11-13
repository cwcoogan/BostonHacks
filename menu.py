"""
    FUNCTION -- Menu()

    Parameter - Null

    Returns -- user_choice int value of like/dislike/super-like

    Notes -- We will need to alter this from L/D/S to the actual physical swipe value 
"""

from movies import *

preference = {
    'like':[],
    'dislike':[],
    'superlike':[]
}

def menu():
    temp_list = ["Frozen","dairy", "water", "Bread", "cheese","Frozen","dairy"]
    
    for j in temp_list:
        user_choice = input(f"Welcome to Food Tinder:\nL: Like \nD: Dislike\nS: Super Like\nFood choice is: {j}\n")   
    
        if user_choice.upper() == "L" and j not in preference['like']:
            preference['like'].append(j)


        elif user_choice.upper() == "D" and j not in preference['dislike']:
            preference['dislike'].append(j)

            if j in preference['like']:
                preference['like'].remove(j)  
            
        elif user_choice.upper() == "S":
            preference['superlike'].append(j)

            if j in preference['like']:
                preference['like'].remove(j)
        print(preference)
        
menu()
    