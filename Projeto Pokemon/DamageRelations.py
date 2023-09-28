import requests

class TipoPokemon:
    __nome= ''
    __endpoint_type_PK = ''
    __double_damage_from = []
    __double_damage_to = []
    __half_damage_from = []
    __half_damage_to = []
    __no_damage_from = []
    __no_damage_to = []

    def endpoints_type(data):
        for endpoint_type_PK in data['types']:
            endpoint_type_PK = endpoint_type_PK['type']['url']
            resposta_type_PK = requests.get(endpoint_type_PK)
            data_type = resposta_type_PK.json()

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

                    