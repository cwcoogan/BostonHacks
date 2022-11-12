# globals for now, can change to local as needed.. 



def menu(): 
    """
    FUNCTION -- Menu()

    Parameter - Null

    Returns -- user_choice int value of like/dislike/super-like

    Notes -- We will need to alter this from L/D/S to the actual physical swipe value 
    """

    like = 1
    dislike = 2
    super_like = 3

    user_choice = input("Welcome to Food Tinder:\nL: Like \nD: Dislike\n"
    "S: Super Like")     
    if user_choice.upper() == "L":
        return like
    elif user_choice.upper() == "D":
        return dislike
    elif user_choice.upper() == "S":
        return super_like
menu()

     




    