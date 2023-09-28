from Pokemon import MeuPokemon
from DamageRelations import TipoPokemon

import requests

print(' BEM VINDO A POKEDEX ')
verificacao = False
while verificacao == False:
    numero_pokemon = int(input('Insira o número do Pokemon desejado\n'))
    if numero_pokemon >= 1 and numero_pokemon <= 905:
        verificacao = True
    else:
        print('Por favor insira um número entre 1 e 905')

endpoint = f'https://pokeapi.co/api/v2/pokemon/{numero_pokemon}'
resposta_da_API = requests.get(endpoint)

data = resposta_da_API.json()

pokemon = MeuPokemon
nome = pokemon.get_nome_pokemon(data)
imagem = pokemon.get_image_pokemom(data)
golpes = pokemon.get_golpes_pokemon(data)
status = pokemon.get_status_pokemon(data)
tipos =  pokemon.get_tipos_pokemon(data)

print(nome)
print(imagem)
print(golpes)
print(status)
print(tipos)


