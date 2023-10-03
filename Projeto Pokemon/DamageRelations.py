import requests

class TypePokemon:
    __datas_type_PK = []
    __double_damage_from = []
    __double_damage_to = []
    __half_damage_from = []
    __half_damage_to = []
    __no_damage_from = []
    __no_damage_to = []
    

    def get_datas_type(data):
        for endpoint_type_PK in data['types']:
            endpoint_type_PK = endpoint_type_PK['type']['url']
            resposta_type_PK = requests.get(endpoint_type_PK)
            data_type = resposta_type_PK.json()
            TypePokemon.__datas_type_PK.append(data_type)
        return TypePokemon.__datas_type_PK
    
    def clear_datas_type(datas_list):
        datas_list.clear()
        TypePokemon.__datas_type_PK = datas_list
        return datas_list
    
    def get_damage_list(data_type):
        for damage_relation in data_type['damage_relations']:
                for relation in data_type['damage_relations'][damage_relation]:
                    name = relation ['name']
                    if damage_relation == 'double_damage_from':
                        TypePokemon.__double_damage_from.append(name)
                    elif damage_relation == 'double_damage_to':
                        TypePokemon.__double_damage_to.append(name)
                    elif damage_relation == 'half_damage_from':
                        TypePokemon.__half_damage_from.append(name)
                    elif damage_relation == 'half_damage_to':
                        TypePokemon.__half_damage_to.append(name)
                    elif damage_relation == 'no_damage_from':
                        TypePokemon.__no_damage_from.append(name)
                    elif damage_relation == 'no_damage_to':
                        TypePokemon.__no_damage_to.append(name)
        damage_list = [TypePokemon.__double_damage_from, TypePokemon.__double_damage_to, 
                       TypePokemon.__half_damage_from, TypePokemon.__half_damage_to,
                       TypePokemon.__no_damage_from, TypePokemon.__no_damage_to]
        return damage_list


    
    def print_damage_list(type, damage_list):
        print(f'O seu pokemon do tipo ', type, ' recebe dobro de dano para      \n' , damage_list[0])
        print(f'O seu pokemon do tipo ', type, ' causa dobro de dano em         \n' , damage_list[1])
        print(f'O seu pokemon do tipo ', type, ' recebe metade de dano para     \n' , damage_list[2])
        print(f'O seu pokemon do tipo ', type, ' causa metade do dano em        \n' , damage_list[3])
        print(f'O seu pokemon do tipo ', type, ' é imune aos danos dos tipos    \n' , damage_list[4])
        print(f'O seu pokemon do tipo ', type, ' não causa aos danos dos tipos  \n' , damage_list[5],'\n ----------------------------------------------------------------------------------------------')
        
    def clear_damage_list(list):
        for clear_damage_list in list:
            list = clear_damage_list.clear()
            TypePokemon.__double_damage_from = []
            TypePokemon.__double_damage_to = []
            TypePokemon.__half_damage_from = []
            TypePokemon.__half_damage_to = []
            TypePokemon.__no_damage_from = []
            TypePokemon.__no_damage_to = []
            return list
    

            

                    