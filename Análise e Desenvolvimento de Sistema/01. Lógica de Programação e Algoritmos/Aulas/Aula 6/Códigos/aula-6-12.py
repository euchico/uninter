game = {'nome':[], 'videogame':[], 'ano':[]}

for i in range(3):
  nome = input('Qual o nome do jogo? ')
  videogame = input('Para qual videogame ele foi lançado? ')
  ano = input('Qual o ano de lançamento? ')
  game['nome'].append(nome)
  game['videogame'].append(videogame)
  game['ano'].append(ano)

print('-' * 20)
print(games)