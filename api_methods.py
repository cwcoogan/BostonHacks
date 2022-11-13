import requests
from random import randint

TOKEN = "eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXBpLmtyb2dlci5jb20vdjEvLndlbGwta25vd24vandrcy5qc29uIiwia2lkIjoiWjRGZDNtc2tJSDg4aXJ0N0xCNWM2Zz09IiwidHlwIjoiSldUIn0.eyJhdWQiOiJidWhhY2tzLWUyMDY3OWE0YWVkOGUzNGI5OTVlODFiOTZjOWUzNWE4OTIyNDkyNzYzNzM3MTI2NzczIiwiZXhwIjoxNjY4MzA4NjU2LCJpYXQiOjE2NjgzMDY4NTEsImlzcyI6ImFwaS5rcm9nZXIuY29tIiwic3ViIjoiYTg3MDgzODMtMmNiMS01ZWJjLWI4OTktODliMTk0OTA0MjE1Iiwic2NvcGUiOiJwcm9kdWN0LmNvbXBhY3QiLCJhdXRoQXQiOjE2NjgzMDY4NTY5MTA4MTY0NDEsImF6cCI6ImJ1aGFja3MtZTIwNjc5YTRhZWQ4ZTM0Yjk5NWU4MWI5NmM5ZTM1YTg5MjI0OTI3NjM3MzcxMjY3NzMifQ.PjxnGnqnO6NicsYZs_7jLd44AzkuK38jr3ay4tvwwuxEKokM8Yfsf8nBUxcKoo8pIbMSf2kRERkRMwzR2IeDW6hR8XsckyiKt1G0cPKfu16VAmZhkIMljkYfFtenJ8nouRkHa2RkLIPCkN5B45gZn_QnQY9un055DgFAmJVw1ReVTFTheAfpkL7xtROUDHZcTicEkXD-T283VkdQHG76Z8eVmQGJsheLr94Y_6FKmTAtKSIVttWOkB2iianb7Lg-YB19tWN0MQvW5Xgh_ZoBDN5vrnwEPQi_oQuIemS2Lg7tPtTYtjjdyPYOXHV7jOzKIOapQXesnD8uJbXaNgcDZA"
START_TERMS = ["food", "ice cream", "chips", "milk", "dairy", "cleaning"]

PRODUCT_URL = f"https://api.kroger.com/v1/products"   


def generate_dict(name, bio, img_file, categories):
    return {
        "name": name, 
        "bio" : bio, 
        "img_file": img_file,
        "categories" : categories
        }

def get_random_item(data): 
    n = randint(1, len(data) - 1)
    return data[n][n]

def generate_data(API_URL, TOKEN, START_TERMS):
    
    header = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {TOKEN}"
    } 
      
    data = []
    for term in START_TERMS:
        parameters = {
            "filter.term" : term
        }
        response = requests.get(API_URL, params=parameters, headers=header)
        response = response.json()["data"]
        data.append(response)
        
    
    return data
    
def get_single_item():
    
    data = generate_data(PRODUCT_URL, TOKEN, START_TERMS)

    item = get_random_item(data)

    name = item["description"]
    bio = "This is a default bio"
    categories = item["categories"].append(item["brand"])
    img = item["image"]

    return generate_dict(name, bio, img, categories)

'''
Call get_single_item() in main
Requires no parameter
Returns a dictionary like so:

{ 
    "name" : "Food Name",
    "bio" : "This is a food bio, 100 characters",
    "img_file" : "food_img.jpg",
    "categories" = ["Frozen", "Dairy"]
}
'''