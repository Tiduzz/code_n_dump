import requests
from PIL import Image
import urllib.request

def returns_pokemon_data(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados = response.json()
    return dados

if __name__ == '__main__':
    dados = returns_pokemon_data('flareon')
    print(dados['sprites']['front_shiny'])
    urllib.request.urlretrieve(dados['sprites']['front_shiny'], "image.png")
    img = Image.open("image.png")
    img.show()