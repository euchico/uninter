# Exercício 1

a = int(input('Digite o 1º lado do triângulo: '))
b = int(input('Digite o 2º lado do triângulo: '))
c = int(input('Digite o 3º lado do triângulo: '))

if ((a > 0) or (b > 0) or (c > 0)):
  if (((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
    # Se você chegou atpe aqui, é porque o triângulo é válido!
    if ((a != b) and (a != c) and (b != c)):
      print('Triângulo escaleno!')
    else:
      if ((a == b) and (a == c) and (b == c)):
        print('Triângulo equilátero!')
      else:
        print('Triângulo isósceles!')
  else:
    print('Ao menos um dos valores indicados não serve para formar um triângulo')
else:
  print('Ao menos um dos valores indicados não serve para formar um triângulo')
