import random
from pprint import pprint
from imdb_api import *

def generate_dict(name, bio, id, genres):
    return {
        "name": name, 
        "bio" : bio, 
        "genres" : genres,
        "id" : id
        }

def get_random_item(movies_dict): 
    i = random.randint(1, len(movies_dict))
    count = 0
    for each in movies_dict: 
        if count != i:
            key = each
            count += 1
    return movies_dict[key]
    
def get_single_item(movies_dict):

    movie = get_random_item(movies_dict)
    name = movie["title"]
    bio = movie["bio"]
    genres = movie["genres"]
    id = movie["id"]

    img_url = movie["img"]
    with open(name + '.jpg', 'wb') as file:
        image = requests.get(img_url).content
        file.write(image)

    return generate_dict(name, bio, id, genres)