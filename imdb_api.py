import requests
from pprint import pprint

# Get Data from API with movie search.
DATA_API_URL = "https://imdb8.p.rapidapi.com/title/find"
GENRE_URL = "https://imdb8.p.rapidapi.com/title/get-genres"
BIO_URL = "https://imdb8.p.rapidapi.com/title/get-taglines"
RATINGS_URL = "https://imdb8.p.rapidapi.com/title/get-ratings"


def get_data():
    params = {
        "q": "movie"
        }

    headers = {
        "X-RapidAPI-Key": "5238b2b59bmsh2ca28605277e0b3p161ad3jsn4ab3133bcba9",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(DATA_API_URL, headers=headers, params=params).json()
    movie_responses = response["results"]
    movies_dict = {}
    count = 0
    for movie in movie_responses:
        if count == 5: break
        count += 1
        id = movie["id"][7:-1]
            
        if "title" not in movie: continue
        
        movies_dict[id] = {}

        # Do image add
        movies_dict[id]["img"] = movie["image"]["url"]

        movies_dict[id]["title"] = movie["title"]
        
        id_params = {"tconst": id}
        
        # Get data using ID
        genres = requests.get(GENRE_URL, headers=headers, params=id_params)
        bio = requests.get(BIO_URL , headers=headers, params=id_params)
        ratings = requests.get(RATINGS_URL, headers=headers, params=id_params)
        
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
    return movies_dict  