from Pokemon import MyPokemon
from DamageRelations import TypePokemon

import requests

print('------- BEM VINDO A POKEDEX -------')
print('###################################')
repeat = True

while repeat == True:
    verification = False
    while verification == False:
        poker_number = int(input('Insira o número do Pokemon desejado...\n'))
        if poker_number >= 1 and poker_number <= 905:
            verification = True
        else:
            print('Por favor insira um número entre 1 e 905')

    endpoint = f'https://pokeapi.co/api/v2/pokemon/{poker_number}'
    api_response = requests.get(endpoint)

    data = api_response.json()

    pokemon = MyPokemon
    name = pokemon.get_nome_pokemon(data)
    image = pokemon.get_image_pokemom(data)
    moves = pokemon.get_golpes_pokemon(data)
    status = pokemon.get_status_pokemon(data)
    types =  pokemon.get_tipos_pokemon(data)
    pokemon_descripion = [name, image, moves, status, types]

    datas_type = TypePokemon.get_datas_type(data)

    pokemon.print_pokemon_description(pokemon_descripion)

    i=0
    for damage_list in datas_type:
        damage_list = TypePokemon.get_damage_list(datas_type[i])
        TypePokemon.print_damage_list(types[i], damage_list)
        i += 1
    print('fonte: ', endpoint)
    loop = True
    while loop == True:
        response = input('Deseja pesquisar por outro pokemon??\n S (sim)     ou      N (não)')
        if response == 's' or response == 'S':
            repeat = True
            loop   = False
        elif response == 'n' or response == 'N':
            repeat = False
            loop   = False
        else:
            print('Por favor insira uma resposta válida!')
            loop = True
