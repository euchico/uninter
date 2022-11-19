print('Bem-vindo a pizzaria do Francisco de Paula Neto')

print('------------------------- CARDÁPIO -------------------------')
print('| CÓDIGO | DESCRIÇÃO  | PIZZA MÉDIA (M) | PIZZA GRANDE (G) |')
print('|     21 | Napolitana |        R$ 20,00 |         R$ 26,00 |')
print('|     22 | Margharita |        R$ 20,00 |         R$ 26,00 |')
print('|     23 | Calabresa  |        R$ 25,00 |         R$ 32,50 |')
print('|     24 | Toscana    |        R$ 30,00 |         R$ 39,00 |')
print('|     25 | Portuguesa |        R$ 30,00 |         R$ 39,00 |')
print('------------------------------------------------------------')

acumulador = 0

while (True):
  tamanho = input('Entre com o tamanho de pizza desejado (M/G): ')
  if ((tamanho != 'M') and (tamanho != 'G')):
    print('Opção Inválida. Pare de digitar tamanhos que não existem!')
    continue

  codigo = input('Entre com o código de pizza desejado (21/22/23/24/25): ')
  if ((codigo != '21') and (codigo != '22') and (codigo != '23') and (codigo != '24') and (codigo != '25')):
    print('Opção Inválida. Pare de digitar códigos que não existem!')
    continue

  if ((codigo == '21') and (tamanho == 'M')):
    print('Você escolheu a pizza Napolitana tamanho M')
    acumulador += 20
  elif ((codigo == '21') and (tamanho == 'G')):
    print('Você escolheu a pizza Napolitana tamanho G')
    acumulador += 26

  // (...)

  pedirMais = input('Deseja pedir mais alguma pizza (S/N)? ')
  if (pedirMais == 'S'):
    continue
  else:
    print('O valor total a ser pago: R${}'.format(acumulador))
    break
