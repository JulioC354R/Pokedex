#importar a biblioteca requests

import requests

print ('GitHub Users')

#Criando variável e recebendo um valor
username = input('Qual o nome do usuário?')

#definindo a URL da API
url =  f'https://api.github.com/users/{username}'

#Recebendo a resposta da API e armazenando em response(utilizamos o requests.get)
response =  requests.get(url)

#a resposta que vem no formato .json é armazenado em data
data = response.json()


#se o status da resposta for 200 imprimir formatando
if response.status_code == 200:

    #aqui  ele busca a informação que no .json foi passada como name
    print(f'Nome completo: {data["name"]}')
else: 
    print('não foi possível encontrar o usuário')
    