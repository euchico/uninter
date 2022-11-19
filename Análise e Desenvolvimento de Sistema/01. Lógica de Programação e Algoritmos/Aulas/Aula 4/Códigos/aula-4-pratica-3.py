# Exercício 1.1

print('CALCULADORA')

print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

operacao = input('Qual operação deseja fazer? ')
if ((operacao == '+') or (operacao == '-') or (operacao == '*') or (operacao == '/')):
  x = int(input('Digite o primeiro valor: '))
  y = int(input('Digite o segundo valor: '))

while (operacao != 's'):
  if (operacao == '+'):
    resultado = x + y
    print('Resultado {} + {} = {}'.format(x, y, resultado))
  elif (operacao == '-'):
    resultado = x - y
    print('Resultado {} - {} = {}'.format(x, y, resultado))
  elif (operacao == '*'):
    resultado = x * y
    print('Resultado {} * {} = {}'.format(x, y, resultado))
  elif (operacao == '/'):
    resultado = x / y
    print('Resultado {} / {} = {}'.format(x, y, resultado))
  else:
    print('Operação inválida.')

  operacao = input('Qual operação deseja fazer? ')
  if ((operacao == '+') or (operacao == '-') or (operacao == '*') or (operacao == '/')):
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

print('Encerrando o program...')
