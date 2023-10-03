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
    moves = pokemon.get_moves_pokemon(data)
    stats = pokemon.get_stats_pokemon(data)
    types =  pokemon.get_types_pokemon(data)
    pokemon_descripion = [name, image, moves, stats, types]

    datas_type = TypePokemon.get_datas_type(data)

    pokemon.print_pokemon_description(pokemon_descripion)

    i=0
    for damage_list in datas_type:
        damage_list = TypePokemon.get_damage_list(datas_type[i])
        TypePokemon.print_damage_list(types[i], damage_list)
        TypePokemon.clear_damage_list(damage_list)
        damage_list = damage_list.clear()
        i += 1
    print('fonte: ', endpoint , '\n')


    moves = pokemon.clear_moves(moves)
    stats = pokemon.clear_stats(stats)
    types = pokemon.clear_types(types)
    datas_type = TypePokemon.clear_datas_type(datas_type)
    damage_list = []
    
    loop = True
    while loop == True:
        response = input('Deseja pesquisar por outro pokemon??\n S (sim)     ou      N (não)\n')
        if response == 's' or response == 'S':
            repeat = True
            loop   = False
        elif response == 'n' or response == 'N':
            repeat = False
            loop   = False
        else:
            print('Por favor insira uma resposta válida!')
            loop = True
