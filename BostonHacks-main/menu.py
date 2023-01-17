"""
    FUNCTION -- Menu()

    Parameter - Null

    Returns -- user_choice int value of like/dislike/super-like

    Notes -- We will need to alter this from L/D/S to the actual physical swipe value 
"""
def menu(genres, user_choice):
    preference = {
        'like':[],
        'dislike':[],
    }
    
    for j in genres:
    
        if user_choice.upper() == "L":
            preference['like'].append(j)


        elif user_choice.upper() == "D" and j not in preference['dislike']:
            preference['dislike'].append(j)
            
        # If it is super like, then it adds 2 instances of the
        # genre in the likes so it is more 
        # likely to get picked
        elif user_choice.upper() == "S":
            preference['like'].append(j)
            preference['like'].append(j)
                
    return preference    