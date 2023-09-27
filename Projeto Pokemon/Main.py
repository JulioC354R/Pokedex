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
    for move in data['moves']:
        golpe = move['move']['name']
        print(f'Golpes: ', golpe)
        print(golpe)

print(f'TIPO: ' , type(golpe))

