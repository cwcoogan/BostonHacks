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
        'superlike':[]
    }
    
    for j in genres:
    
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
    return preference    