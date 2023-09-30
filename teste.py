moves = [
    'razor-wind', 'swords-dance', 'cut', 'bind', 'vine-whip', 'headbutt', 'tackle', 'body-slam',
    'take-down', 'double-edge', 'growl', 'strength', 'mega-drain', 'leech-seed', 'growth', 
    'razor-leaf', 'solar-beam', 'poison-powder', 'sleep-powder', 'petal-dance', 'string-shot', 
    'toxic', 'rage', 'mimic', 'double-team', 'defense-curl', 'light-screen', 'reflect', 'bide', 
    'sludge', 'skull-bash', 'amnesia', 'flash', 'rest', 'substitute', 'snore', 'curse', 'protect', 
    'sludge-bomb', 'mud-slap', 'outrage', 'giga-drain', 'endure', 'charm', 'false-swipe', 'swagger', 
    'fury-cutter', 'attract', 'sleep-talk', 'return', 'frustration', 'safeguard', 'sweet-scent', 
    'synthesis', 'hidden-power', 'sunny-day', 'rock-smash', 'facade', 'nature-power', 'helping-hand', 
    'ingrain', 'knock-off', 'secret-power', 'weather-ball', 'grass-whistle', 'bullet-seed', 'magical-leaf', 
    'natural-gift', 'worry-seed', 'seed-bomb', 'energy-ball', 'leaf-storm', 'power-whip', 'captivate', 
    'grass-knot', 'venosh', 'grass-pledge', 'work-up', 'grassy-terrain', 'confide', 'grassy-glide'
]

# Número de golpes por linha
golpes_por_linha = 5

# Imprimir os golpes
for i, move in enumerate(moves, start=1):
    print(f"{move:<15}", end="")
    if i % golpes_por_linha == 0:
        print()

# Adicionar uma quebra de linha se o número total de golpes não for um múltiplo de golpes_por_linha
if len(moves) % golpes_por_linha != 0:
    print()
