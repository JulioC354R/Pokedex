# Pokedex by JulioC354R
Faça um programa que leia o número da pokedex de um Pokémon, este
número deve estar entre o intervalo de 1 e 905. Seu programa irá ler esse número e fazer uma
requisição na api: https://pokeapi.co/api/v2/pokemon/1 . Para mais detalhes sobre a api, consultar
link: https://pokeapi.co. Baseado neste número informado pelo usuário, seu programa deverá
retornar:
## Primeira fase:
- Retorne o nome do Pokémon;
- Retorne o link do front_default do Pokémon (link da foto frontal);
## Segunda fase:
- Retorne uma lista contendo todos os golpes do Pokémon
- Retorne um único dicionário contendo apenas o stats e o nome do stats, exemplo:
![image](https://github.com/JulioC354R/Pokedex/assets/92527708/505ab5b1-9628-4047-83ae-95d2670f5f39)

Para cada Pokémon, teremos seu stats sendo retornado dessa maneira, para este a
exemplo da foto, a saída esperada será um dicionário no seguinte modelo:
![image](https://github.com/JulioC354R/Pokedex/assets/92527708/59917b48-6033-4811-9695-e98b37013a31)

Obs.: Deverá funcionar dinamicamente para todos os stats que aquele Pokémon tiver.

## Terceira fase:
- Tipo ou tipos do Pokémon;
- Baseado no Pokémon escolhido pelo usuário, o Pokémon poderá ter 1 ou 2 tipos. Você deverá
fazer outra requisição no link disponibilizado na chave types da api para cada tipo e retornar o
double_damage_from, double_damage_to, no_damage_from e no_damage_to como no
exemplo abaixo:
Na api, para entrada 1, o retorno de types será:
![image](https://github.com/JulioC354R/Pokedex/assets/92527708/6dd68858-7540-483b-ad5e-d2486aacf27f)


Então deverá ser retornado, dessas URL’s, em uma lista, referente ao tipo do pokémon
escolhido pelo usuário, as informações relacionadas ao nome de double_damage_from,
double_damage_to, no_damage_from e no_damage_to.

Exemplo esperado de entrada do programa (número do pokémon): 1

Exemplo esperado de saída do programa (como bulbassaur tem dois tipos: grass e poison):

Leva dano duplo para: [&#39;Tipo do seu pokémon grass : Leva double damage para lying&#39;,&#39;Tipo do seu pokémon poison : 
Leva double damage para ground&#39;]

Realiza dano duplo em: [&#39;Tipo do seu pokémon grass: dá double damage em ground&#39;,
&#39;Tipo do seu pokémon poison : dá double damage em grass&#39;]

Não toma dano de: [&#39;Tipo do seu pokémon grass :Todos os pokémon podem causar certo tipo
de dano a este tipo&#39;, &#39;Tipo do seu pokémon poison :Todos os pokémon podem causar
certo tipo de dano a este tipo&#39;]

Não gera dano em: [&#39;Tipo do seu pokémon grass: Nenhum pokémon é imune a este tipo&#39;,
&#39;Tipo do seu pokémon poison : não dá dano no tipo steel&#39;]



![image](https://github.com/JulioC354R/Pokedex/assets/92527708/f03cc812-e5c7-4fb2-9438-fa02d524c8ce)
