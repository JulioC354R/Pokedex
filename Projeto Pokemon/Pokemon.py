class MyPokemon:
    __name = ''
    __image = ''
    __moves= []
    __stats = []
    __types =[]

    def get_nome_pokemon(data):
        MyPokemon.__name = data["forms"] [0]['name']
        return MyPokemon.__name
    def get_image_pokemom(data):
        MyPokemon.__image = data["sprites"]["front_default"]
        return MyPokemon.__image
    
    def get_moves_pokemon(data):
        for move in data['moves']:
            move = move['move']['name']
            MyPokemon.__moves.append(move)
        return MyPokemon.__moves
    
    def clear_moves(moves_list):
        moves_list.clear()
        MyPokemon.__moves = moves_list
        return moves_list


    def get_stats_pokemon(data):
        for stats in data['stats']: 
            nome_status = stats['stat']['name']
            status_base = stats['base_stat']
            MyPokemon.__stats.append(nome_status)
            MyPokemon.__stats.append(status_base)
        return MyPokemon.__stats
    
    def clear_stats(stats_list):
        stats_list.clear()
        MyPokemon.__stats = stats_list
        return stats_list

    
    def get_types_pokemon(data):
        for types in data['types']:
            type_pokemon = types['type']['name']
            MyPokemon.__types.append(type_pokemon)
        return MyPokemon.__types

    def clear_types(types_list):
        types_list.clear()
        MyPokemon.__types = types_list
        return types_list
    
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
        
        stats = desc[3]
        print(f'Status Base do '     , desc[0], ':\n', 
            'HP:          ', stats[1],     '      ATK:         ', stats[3] ,'      DEF:   ', stats[5], '\n',
            'SPECIAL ATK: ', stats[7],     '      SPECIAL DEF: ', stats[9] ,'      Speed: ', stats[11], '\n',  line)
        print(f'Tipos do Pokemon '   , desc[0], ':\n', desc[4],'\n ', line)