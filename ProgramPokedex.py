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
pk_stats_name = []
pk_stats_base = []
pk_stats = []
pk_types = []
url_types = []
types_limit = 2
double_damage_from = []
double_damage_to = []
no_damage_from = []
no_damage_to = []

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


print(f'Nome do Pokemon: {pk_name}\n')
print(f'Image Frontal do {pk_name}:\n {pk_image}\n')


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
                            pk_stats_name.append(value_stat)
                if keys_stats == 'base_stat':
                    pk_stats_base.append(value_stats)

for i in range(len(pk_stats_base)):
    pk_stats.append(pk_stats_name[i])
    pk_stats.append(pk_stats_base[i])
    i =+ 1


print(f'Lista de golpes do {pk_name}: \n {pk_moves} \n')
print(f'Base Stats do {pk_name} \n {pk_stats} \n')

print('#############        DESAFIO 3       ###############\n\n')

for key, value in data.items():
    if key == 'types':
        for element_types in value:
            for key_types, value_types in element_types.items():
                if key_types == 'type':
                    for key_type, value_type in value_types.items():
                        if key_type == 'name':
                            if len(pk_types) <= types_limit:
                                pk_types.append(value_type)
                        if key_type == 'url':
                            if len(url_types) <= types_limit:
                                url_types.append(value_type)


print(f'Tipos do pokemon {pk_name}: {pk_types} \n')


i = 0
for url in url_types:
    type_response = requests.get(url_types[i])
    data_type = type_response.json()
    for keysDT, valuesDT in data_type.items():
        if keysDT == 'damage_relations':
            
            for keysDR, valuesDR in valuesDT.items():
                if keysDR == 'double_damage_from':
                    for elementDR in valuesDR:
                        for keyDDF, valueDDF in elementDR.items():
                            if keyDDF == 'name':
                                double_damage_from.append(valueDDF)

                if keysDR == 'double_damage_to':
                    for elementDR in valuesDR:
                        for keyDDT, valueDDT in elementDR.items():
                            if keyDDT == 'name':
                                double_damage_to.append(valueDDT)
                
                if keysDR == 'no_damage_from':
                    for elementDR in valuesDR:
                        for keyNDF, valueNDF in elementDR.items():
                            if keyNDF == 'name':
                                no_damage_from.append(valueNDF)
                
                if keysDR == 'no_damage_to':
                    for elementDR in valuesDR:
                        for keyNDT, valueNDT in elementDR.items():
                            if keyNDT == 'name':
                                no_damage_to.append(valueNDT)
    print(f'Seu pokemon do tipo {pk_types[i]} toma dobro de dano para: \n', double_damage_from, '\n')
    print(f'Seu pokemon do tipo {pk_types[i]} causa dobro de dano em : \n', double_damage_to, '\n')
    print(f'Seu pokemon do tipo {pk_types[i]} não leva dano para: \n', no_damage_from, '\n')
    print(f'Seu pokemon do tipo {pk_types[i]} não causa dano para: \n', no_damage_to, '\n')


    double_damage_from.clear()
    double_damage_to.clear()
    no_damage_from.clear()
    no_damage_to.clear()
    i =+ 1