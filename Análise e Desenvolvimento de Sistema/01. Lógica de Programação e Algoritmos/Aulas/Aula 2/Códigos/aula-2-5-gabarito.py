# Exercício 2.1
x = int(input('Digite um número inteiro: '))
y = int(input('Digite outro número inteiro: '))
# Maneira Clássica
res = 'O resultado da soma de %i com %i é %i.'  % (x, y, x + y)
print(res)
# Maneira Moderna
res = 'O resultado da soma de {} com {} é {}.'.format(x, y, x + y)
print(res)