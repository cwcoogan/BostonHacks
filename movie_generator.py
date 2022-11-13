import random
from pprint import pprint
from imdb_api import *


def generate_dict(name, bio, img_file, genres):
    return {
        "name": name, 
        "bio" : bio, 
        "img_file": img_file,
        "genres" : genres
        }

def get_random_item(movies_dict): 
    print("done")
    # pprint(movies_dict)
    
    i = random.randint(1, len(movies_dict))
    count = 0
    for each in movies_dict: 
        if count != i:
            key = each
            count += 1
    return movies_dict[key]
    
def get_single_item():
    
    movies_dict = get_data()

    movie = get_random_item(movies_dict)
    name = movie["title"]
    bio = movie["bio"]
    genres = movie["genres"]

    
    # # TODO: Add Image
    # img = item["images"][0]["sizes"][4]["url"]
    # image_file = create_image_file(img)
    
    img = "test.jpg"

    return generate_dict(name, bio, img, genres)

item = get_single_item()
print(item)