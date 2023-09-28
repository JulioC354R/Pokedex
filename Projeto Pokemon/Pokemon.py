class MeuPokemon:
    __name = ''
    __image = ''
    __moves= []
    __status = []
    __types =[]

    def get_nome_pokemon(data):
        MeuPokemon.__name = data["forms"] [0]['name']
        return MeuPokemon.__name
    def get_image_pokemom(data):
        MeuPokemon.__image = data["sprites"]["front_default"]
        return MeuPokemon.__image
    
    def get_golpes_pokemon(data):
        for move in data['moves']:
            golpe = move['move']['name']
            MeuPokemon.__moves.append(golpe)
        return MeuPokemon.__moves


    def get_status_pokemon(data):
        for stats in data['stats']: 
            nome_status = stats['stat']['name']
            status_base = stats['base_stat']
            MeuPokemon.__status.append(nome_status)
            MeuPokemon.__status.append(status_base)
        return MeuPokemon.__status
    
    def get_tipos_pokemon(data):
        for types in data['types']:
            type_pokemon = types['type']['name']
            MeuPokemon.__types.append(type_pokemon)
        return MeuPokemon.__types

    