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
            
