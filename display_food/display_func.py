from Food import Food
dict = {}
def display_function(food_object: str, bio: str, keys_list: set):
    """Inputs """
    dict[food_object] = {'bio' : bio, 'Key' : keys_list}
    print(dict)
    return dict

food1 = Food("Chicken tenders")
food1.set_bio("Juicy chicken tenders")
food1.set_categories("Honey")
# food1.set_categories("Jolly")
print(food1.get_name()) # Chicken tenders
print(food1.get_bio()) # Juicy chicken tenders
print(food1.get_categories()) # Honey
food_object_list = []
food_object_list.append(food1.get_name())

food2 = Food("Grill Chicken")
food2.set_bio("Awesome grilled chicken")
food2.set_categories("Smooth")
food_object_list.append(food2.get_name())

display_function(food1.get_name(), food1.get_bio(), food1.get_categories())
display_function(food2.get_name(), food2.get_bio(), food2.get_categories())