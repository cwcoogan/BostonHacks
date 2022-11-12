import requests
from pprint import pprint
from random import randint

# url = "https://api.kroger.com/v1/connect/oauth2/authorize"

# p = {
#     "grant_type": "client_credentials",
#     "scope": "product.compact",
#     "client_id": "buhacks-e20679a4aed8e34b995e81b96c9e35a8922492763737126773",
#     "client_secret": "7QX7xgzoLmtFFTKhv0tvHDH6mlwGmHhC17sFGEt4",
#     "response_type": "code",
#     "redirect_uri": "https://localhost"
# }
TOKEN = "eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXBpLmtyb2dlci5jb20vdjEvLndlbGwta25vd24vandrcy5qc29uIiwia2lkIjoiWjRGZDNtc2tJSDg4aXJ0N0xCNWM2Zz09IiwidHlwIjoiSldUIn0.eyJhdWQiOiJidWhhY2tzLWUyMDY3OWE0YWVkOGUzNGI5OTVlODFiOTZjOWUzNWE4OTIyNDkyNzYzNzM3MTI2NzczIiwiZXhwIjoxNjY4Mjk3NjA1LCJpYXQiOjE2NjgyOTU4MDAsImlzcyI6ImFwaS5rcm9nZXIuY29tIiwic3ViIjoiYTg3MDgzODMtMmNiMS01ZWJjLWI4OTktODliMTk0OTA0MjE1Iiwic2NvcGUiOiJwcm9kdWN0LmNvbXBhY3QiLCJhdXRoQXQiOjE2NjgyOTU4MDU5NjU1NDEzOTYsImF6cCI6ImJ1aGFja3MtZTIwNjc5YTRhZWQ4ZTM0Yjk5NWU4MWI5NmM5ZTM1YTg5MjI0OTI3NjM3MzcxMjY3NzMifQ.S86lX1QsjE6d8twrr9JqqGbnZeIzt1ctVFIjYtRiAzpWHtz2di9D0UwxeYXk_RHHY8rhqkhNRM0xuadhnxiQqcsSf5wcnuBAm1GFgMUUGhFq0Tlw9EhgKVgHnrhSKJ5zVtoCkRVycwMp_I2xTwS7c9JD4N1WiI8Y-9Rv7aQVAzNTCSuNVj11SzV9rB-7GZiGIjyLU43LGrrxyRj40bd8gyZiD2ld0delv6LJta3BbSdywZIk8ESVM0xWvitIC-IPh4lBklgXeUdWTwcKC1AMIRvmSkgi2B1FzVegzj01fxYQC2RGUvuYySiU8KOCYwzLX1ZKC1mgoOciYwwb66PalQ"

terms = ["food", "ice cream", "chips", "milk", "dairy", "cleaning"]


product_url = f"https://api.kroger.com/v1/products"

# img_url = response["data"][0]['images'][0]["sizes"][3]["url"]

# with open("img.jpg", 'wb') as img_file:
#     resp = requests.get(img_url)
#     img_file.write(resp.content)
    
    
'''Generate a dict like
    item = { 
        "name" : "Food Name",
        "bio" : "This is a food bio, 100 characters",
        "img_file" : "food_img.jpg"
    }
'''


def generate_dict(name, bio, img_file):
    return {
        "name": name, 
        "bio" : bio, 
        "img_file": img_file
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
    

data = generate_data(product_url, TOKEN, terms)
# pprint(data)

item = get_random_item(data)

# pprint(item)
print(item["description"])
print(item["categories"])
print(item["brand"])

        
        
