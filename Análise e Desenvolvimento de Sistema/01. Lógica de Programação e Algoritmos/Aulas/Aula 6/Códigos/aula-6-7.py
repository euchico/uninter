mercado = []

for i in range(2):
  nome = input('Digite o nome do item: ')
  qdt = int(input('Digite a quantidade: '))
  valor = float(input('Digite o valor: '))
  mercado.append([nome, qdt, valor])

soma = 0

print('Lista de compras:')
print('-' * 20)
print('item | quantidade | valor unitário | total do item')

for item in mercado:
  print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
  soma += item[1] * item[2]

print('-' * 20)
print('Total a ser pago: {}'.format(soma))