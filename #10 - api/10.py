"""
Making an API call is one of the most common tasks in programming.

Implement an HTTP call to an API of your choice and display its result through the terminal. For example: Pokémon, Marvel...

Here is a list of possible APIs you can explore:
https://github.com/public-apis/public-apis
"""

import requests
from PIL import Image
from io import BytesIO

url = "https://randomfox.ca/floof/"

response = requests.request("GET", url)
print(response.text)

image = requests.request("GET", response.json()["image"])
show_image = Image.open(BytesIO(image.content)).show()
