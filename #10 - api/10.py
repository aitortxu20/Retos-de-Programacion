"""
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
"""

import requests
from PIL import Image
from io import BytesIO

url = "https://randomfox.ca/floof/"

response = requests.request("GET", url)
print(response.text)

image = requests.request("GET", response.json()["image"])
show_image = Image.open(BytesIO(image.content)).show()
