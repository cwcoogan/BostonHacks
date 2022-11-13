import requests
from pprint import pprint
from main import *


# API Access data
headers = {
        "X-RapidAPI-Key": "9e07ffe2d7msh9f15e71ba279840p1311b5jsn533634d6ad40",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

# Get Data from API with movie search.
DATA_API_URL = "https://imdb8.p.rapidapi.com/title/v2/get-popular-movies-by-genre"
DETAILS_URL = "https://imdb8.p.rapidapi.com/title/get-details"
GENRE_URL = "https://imdb8.p.rapidapi.com/title/get-genres"
BIO_URL = "https://imdb8.p.rapidapi.com/title/get-taglines"
RATINGS_URL = "https://imdb8.p.rapidapi.com/title/get-ratings"

POPULAR_GENRES_URL = "https://imdb8.p.rapidapi.com/title/list-popular-genres"

# Default genres to start with
DEFAULT_GENRES = []
genres = requests.get(POPULAR_GENRES_URL, headers=headers).json()
for each in genres["genres"]:
    DEFAULT_GENRES.append(each["description"].lower())

def get_data(genres_list):
    
    if len(genres_list) == 0:
        genres_list = DEFAULT_GENRES
        
    movies_dict = {}
    
    for genre in genres_list[10:15]:
        params = {
            "genre": genre,
            "limit": "3",
            }

        response = requests.get(DATA_API_URL, headers=headers, params=params).json()
        pprint(response)
        for each in response:
            print(each)
            id = each[7:-1]
            id_params = {
                "tconst": id
            }
            
            details = requests.get(DETAILS_URL, headers=headers, params=id_params).json()
            genres = requests.get(GENRE_URL, headers=headers, params=id_params)
            bio = requests.get(BIO_URL , headers=headers, params=id_params)
            ratings = requests.get(RATINGS_URL, headers=headers, params=id_params)
            
            # if "title" not in details: continue
            movies_dict[id] = {}
            
            movies_dict[id]["id"] = id

            movies_dict[id]["img"] = details["image"]["url"]

            movies_dict[id]["title"] = details["title"]
        
            # Set Genres
            movies_dict[id]["genres"] = genres.json()
            
            # Set Ratings
            if "rating" not in ratings.json():
                movies_dict[id]["rating"] = -1
            else:
                movies_dict[id]["rating"] = ratings.json()["rating"]
            
            # Set Taglines
            if "taglines" not in bio.json() or bio.json()["taglines"] == None: 
                movies_dict[id]["bio"] = "A Fun surprise"
            else:
                movies_dict[id]["bio"] = bio.json()["taglines"][0]
                
    print(movies_dict)
    return movies_dict  