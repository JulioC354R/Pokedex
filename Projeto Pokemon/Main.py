#Importando a biblioteca necessária

import requests
import json

#Recebendo o número do pokemon pelo usuário e repetindo a pergunta até que ele insira um número válido

print(' BEM VINDO A POKEDEX ')
verificacao = False
while verificacao == False:
    numero_pokemon = int(input('Insira o número do Pokemon desejado\n'))
    if numero_pokemon >= 1 and numero_pokemon <= 905:
        verificacao = True
    else:
        print('Por favor insira um número entre 1 e 905')

#criando variáveis para simplificar

endpoint = f'https://pokeapi.co/api/v2/pokemon/{numero_pokemon}'
#pega a resposta da API e converte para .json
resposta_da_API = requests.get(endpoint)

#aqui está como dicionário
data = resposta_da_API.json()


#acessando o dicionário forms dentro do json (é aqui que está o nome e uma URL)
dicionario_forms = data["forms"]

#dentro do dicionário, havia uma lista, então precisei tirar a lista do dicionário
lista_name = dicionario_forms [0]
#finalmente consegui acessar o valor que representa name dentro dessa lista
nome_pokemon = lista_name['name']


#Pegando o link da imagem do pokemon: (o link está no dicionário sprites)
dicionario_sprites = data["sprites"]
#tirando da lista sprites o url que corresponde a front_default:
imagem_pokemon = dicionario_sprites["front_default"]



#############   SEGUNDA FASE   #############

#dicionario_moves = data["moves"]
#lista_move = dicionario_moves["move"]["name"]
#golpes_pokemon = lista_move



if resposta_da_API.status_code == 200:
    print(f'Nome do Pokemon: ', nome_pokemon)
    print(f'Imagem: ', imagem_pokemon)

#utilizando o for eu defino move que está dentro do "data" e busco o dicionário moves, dentro dele há dicionários de
#cada golpe, por isso defini o golpe como dentro do move o valor da chave "name"
    lista_golpes = []
    for move in data['moves']:
        golpe = move['move']['name']
        lista_golpes.append(golpe)

    print(f'Golpes: ', lista_golpes)


##########      TERCEIRA FASE       ##############

    lista_status = []
    for stats in data['stats']: 
        nome_status = stats['stat']['name']
        status_base = stats['base_stat']
        lista_status.append(nome_status)
        lista_status.append(status_base)

    print(f'Status do Pokemon: ', lista_status)

    lista_tipos = []
    for types in data['types']:
        tipo_pokemon = types['type']['name']
        lista_tipos.append(tipo_pokemon)
        
    print(f'Tipos do ', nome_pokemon, ': ', lista_tipos)

##########      FASE FINAL      ############

    lista_double_damage_from = []
    lista_double_damage_to = []
    lista_half_damage_from = []
    lista_half_damage_to = []
    lista_no_damage_from = []
    lista_no_damage_to = []

    for endpoint_type_PK in data['types']:
        endpoint_type_PK = endpoint_type_PK['type']['url']
        resposta_type_PK = requests.get(endpoint_type_PK)
        data_type = resposta_type_PK.json()

        #lista dentro de dois dicionarios

        for damage_relation in data_type['damage_relations']:
            for relation in data_type['damage_relations'][damage_relation]:
                name = relation ['name']
                if damage_relation == 'double_damage_from':
                    lista_double_damage_from.append(name)
                elif damage_relation == 'double_damage_to':
                    lista_double_damage_to.append(name)
                elif damage_relation == 'half_damage_from':
                    lista_half_damage_from.append(name)
                elif damage_relation == 'half_damage_to':
                    lista_half_damage_to.append(name)
                elif damage_relation == 'no_damage_from':
                    lista_no_damage_from.append(name)
                elif damage_relation == 'no_damage_to':
                    lista_no_damage_to.append(name)
        print(f'O seu pokemon do tipo ', tipo_pokemon, ' leva dobro de dano para ' , lista_double_damage_from)
        print(f'O seu pokemon do tipo ', tipo_pokemon, ' causa dobro de dano em ' , lista_double_damage_to)
        print(f'O seu pokemon do tipo ', tipo_pokemon, ' leva dano normal em ' , lista_half_damage_from)
        print(f'O seu pokemon do tipo ', tipo_pokemon, ' causa dano normal em ' , lista_half_damage_to)
        print(f'O seu pokemon do tipo ', tipo_pokemon, ' é imune aos danos dos tipos ' , lista_no_damage_from)
        print(f'O seu pokemon do tipo ', tipo_pokemon, ' não causa aos danos dos tipos ' , lista_no_damage_to)