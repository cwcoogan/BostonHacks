"""
Menu Function -- 

Acts as the back-end functionality for liking/disliking food items

Returns -- a list of liked/disliked food
            if super-liked, returns the super-liked food item
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

        




    