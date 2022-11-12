"""
Menu Function -- 

Presents 3 options, like, dislike, super-like to the user

Returns the value selected
"""

like = 1
dislike = 2
super_like = 3

def menu(): 
    user_choice = input("Welcome to Food Tinder:\nL: Like \nD: Dislike\n"
    "S: Super Like")     
    if user_choice.upper() == "L":
        return like
    elif user_choice.upper() == "D":
        return dislike
    elif user_choice.upper() == "S":
        return super_like
menu()

     




    