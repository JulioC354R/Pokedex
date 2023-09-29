class MyPokemon:
    __name = ''
    __image = ''
    __moves= []
    __status = []
    __types =[]

    def get_nome_pokemon(data):
        MyPokemon.__name = data["forms"] [0]['name']
        return MyPokemon.__name
    def get_image_pokemom(data):
        MyPokemon.__image = data["sprites"]["front_default"]
        return MyPokemon.__image
    
    def get_golpes_pokemon(data):
        for move in data['moves']:
            move = move['move']['name']
            MyPokemon.__moves.append(move)
        return MyPokemon.__moves


    def get_status_pokemon(data):
        for stats in data['stats']: 
            nome_status = stats['stat']['name']
            status_base = stats['base_stat']
            MyPokemon.__status.append(nome_status)
            MyPokemon.__status.append(status_base)
        return MyPokemon.__status
    
    def get_tipos_pokemon(data):
        for types in data['types']:
            type_pokemon = types['type']['name']
            MyPokemon.__types.append(type_pokemon)
        return MyPokemon.__types

    def print_pokemon_description(desc):
        line = '----------------------------------------------------------------------------------------------'
        print(f'Nome do Pokemon:                  \n', desc[0],'\n ', line)
        print(f'Imagem do '          , desc[0], ':\n', desc[1],'\n ', line)
        
        print(f'Lista de Golpes do  ', desc[0], ':\n')
        moves_per_line = 7
        moves = desc[2]

        for i, move in enumerate(moves, start=1):
            print(f"{move:<15}", end="")
            if i % moves_per_line == 0:
                print()
        
        if len(moves) % moves_per_line != 0:
            print()
        print(line)
        
        print(f'Status Base do '     , desc[0], ':\n', desc[3], '\n', line)
        print(f'Tipos do Pokemon '   , desc[0], ':\n', desc[4],'\n ', line)