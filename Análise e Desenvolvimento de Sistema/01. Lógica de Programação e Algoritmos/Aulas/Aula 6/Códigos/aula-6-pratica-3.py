# Exercício 1

palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
  print('Palavra: {}. Vogais: '.format(palavra.upper()), end='')
  for letra in palavra:
    if letra.lower() in 'aeiou':
      print(letra.upper(), end=' ')
  print()