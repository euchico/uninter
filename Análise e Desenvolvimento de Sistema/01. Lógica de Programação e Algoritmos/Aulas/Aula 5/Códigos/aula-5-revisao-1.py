#Inicio da função volumeFeijoada()
def volumeFeijoada():
  print('-------------------- Menu 1 de 3 - Volume Feijoada --------------------')
  while True:
    try:
      volumeF = int(input('Digite a quantidade desejada (ml): '))
      if ((volumeF >= 300) and (volumeF <= 5000)):
        return volumeF * 0.08
      else:
        print('Pare de digitar valores abaixo de 300 ou acima de 5000.')
        continue
    except ValueError:
      print('Pare de digitar valores não inteiros')
#Fim da função volumeFeijoada()

#Inicio da função opcaoFeijoada()
def opcaoFeijoada():
  print('-------------------- Menu 2 de 3 - Opção Feijoada --------------------')
  while True:
    opcaoF = input('Qual opção de feijoada desejada \n' + 
                   'b - Básica  (Feijão + Paiol + Costelinha) \n' +
                   'p - Premium (Feijão + Paiol + Costelinha + Partes de Porco) \n' + 
                   's - Suprema (Feijão + Paiol + Costelinha + Partes de Porco + Charque + Calabresa) \n' + 
                   '>> ')
    opcaoF = opcaoF.lower()
    if (opcaoF == 'b'):
      return 1.00
    elif (opcaoF == 'p'):
      return 1.25
    elif (opcaoF == 's'):
      return 1.50
    else:
      print('Pare de digitar opções diferentes de b/p/s')
      continue
#Fim da função opcaoFeijoada()

#Inicio da função acompanhamentoFeijoada()
def acompanhamentoFeijoada():
  print('-------------------- Menu 3 de 3 - Acompanhamento Feijoada --------------------')
  acumulador = 0
  while True:
    acompanhamentoF = input('Deseja mais algum adicional:  \n' + 
                            '0 - Não desejo mais acopanhamentos (encerrar pedido) \n' + 
                            '1 - 200g de arroz \n' +
                            '2 - 150g de farifa especial \n' +
                            '3 - 100g de couve cozida \n' +
                            '4 - 1 laranja descascada \n' +
                            '>> ')
    if (acompanhamentoF == '0'):
      return acumulador
    elif (acompanhamentoF == '1'):
      acumulador += 5
      continue
    elif (acompanhamentoF == '2'):
      acumulador += 6
      continue
    elif (acompanhamentoF == '3'):
      acumulador += 7
      continue
    elif (acompanhamentoF == '4'):
      acumulador += 3
      continue
    else:
      print('Pare de digitar opções diferentes de 0/1/2/3/4/')
      continue
#Fim da função acompanhamentoFeijoada()

#Inicio do Main
print('-------------------- Bem-vindo ao programa de feijoada do Francisco de Paula --------------------')

volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total = ((volume * opcao) + acompanhamento)
print('O total ficou: R$ {:.2f} (Volume R$ {:.2f}, Opção R$ {:.2f}. Acompanhamento R$ {:.2f})'.format(total,volume,opcao,acompanhamento))