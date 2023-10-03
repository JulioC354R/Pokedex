import requests

poke_number = int(input('Insira o número do Pokemon: \n'))
if poke_number < 1 and poke_number > 905:
    while poke_number < 1 and poke_number > 905:
        print('Por favor insira um número entre 1 e 905')
        poke_number = input('Insira o número do Pokemon: \n')


endpoint = (f'https://pokeapi.co/api/v2/pokemon/{poke_number}')
response = requests.get(endpoint)
data = response.json()

pk_name = ''
pk_image = ''
pk_moves = []
pk_stats = []
pk_types= []

print('#############        DESAFIO 1       ###############\n\n')

for keys, value in data.items():
    if keys == 'forms':
        for element_forms in value:
            for keys_forms, value_forms in element_forms.items():
                if keys_forms == 'name':
                    pk_name = value_forms
    
    if keys == 'sprites':
        for keys_sprites, value_sprites in value.items():
            if keys_sprites == 'front_default':
                pk_image = value_sprites


print(pk_name)
print(pk_image)


print('#############        DESAFIO 2       ###############\n\n')

for keys, value in data.items():
    if keys == 'moves':
        for element_moves in value:
            for keys_moves, value_moves in element_moves.items():
                if keys_moves == 'move':
                    for key_move, value_move in value_moves.items():
                        if key_move == 'name':
                            pk_moves.append(value_move)
    if keys == 'stats':
        for element_stats in value:
            for keys_stats, value_stats in element_stats.items():
                if keys_stats == 'stat':
                    for keys_stat, value_stat in value_stats.items():
                        if keys_stat == 'name':
                            pk_stats.append(value_stat)
                if keys_stats == 'base_stat':
                    pk_stats.append(value_stats)

                    
                        

print(pk_moves)
print(pk_stats)

print('#############        DESAFIO 3       ###############\n\n')

for key, value in data.items():
    if key == 'types':
        for element_types in value:
            for key_types, value_types in element_types.items():
                if key_types == 'type':
                    for key_type, value_type in value_types.items():
                        if key_type == 'name':
                            pk_types.append(value_type)


print(pk_types)
