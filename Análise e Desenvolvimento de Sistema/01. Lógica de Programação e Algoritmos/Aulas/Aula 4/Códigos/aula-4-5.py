soma = 0
cont = 1
while (cont <= 5):
  x = int(input('Digite a {}ª nota: '.format(cont)))
  soma += x
  cont += 1

print('Somatório: {}'.format(soma))