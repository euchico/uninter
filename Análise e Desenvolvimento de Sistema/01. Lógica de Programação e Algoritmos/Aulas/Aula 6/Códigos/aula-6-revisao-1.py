# Início das Variáveis Globais --------------- //
lista_produto = []
codigo_produto = 0

# Fim das Variáveis Globais --------------- //

# Início de cadastrar_produto() --------------- //
def cadastrar_produto(codigo):
  print('Bem-vindo ao menu de Cadastrar Produtos')
  print('Código di Produto: {}'.format(codigo))

  nome = input('Entre com o NOME do produto: ')
  fabricante = input('Entre com o FABRICANTE do produto: ')
  preco = int(input('Entre com o PREÇO(R$) do produto: '))
  
  dicionario_produto = {'codigo':codigo, 'nome':nome, 'fabricante':fabricante, 'preco':preco}
  lista_produto.append(dicionario_produto.copy())
# Fim de cadastrar_produto() --------------- //

# Início de consultar_produto() --------------- //
def consultar_produto():
  print('Bem-vindo ao menu de Consultar Produtos')
  while True:
    opcao_consultar = input('Escolha a opção desejada: \n' +
                      '1 - Consultar TODOS os Produtos\n' + 
                      '2 - Consultar Produto por CÓDIGO\n' +
                      '3 - Consultar Produto por FABRICANTE\n' +
                      '4 - Retornar\n' +
                      '>> ')
    print()

    if opcao_principal == '1':
      print('Você escolheu a opção consultar TODOS os Produtos')
      for produto in lista_produto:
        print('--------------------')
        for chave, valor in produto.items():
          print('{}: {}'.format(chave, valor))
        print('--------------------')
    elif opcao_principal == '2':
      print('Você escolheu a opção consultar Produto por CÓDIGO')
      valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
      for produto in lista_produto:
        if produto['codigo'] == valor_desejado:
          print('--------------------')
          for chave, valor in produto.items():
            print('{}: {}'.format(chave, valor))
          print('--------------------')
    elif opcao_principal == '3':
      print('Você escolheu a opção consultar Produto por FABRICANTE')
      valor_desejado = input('Entre com o FABRICANTE desejado: ')
      for produto in lista_produto:
        if produto['fabricante'] == valor_desejado:
          print('--------------------')
          for chave, valor in produto.items():
            print('{}: {}'.format(chave, valor))
          print('--------------------')
    elif opcao_principal == '4':
      return
    else:
      print('Opção Inválida. Tente Novamente...')
      continue
# Fim de consultar_produto() --------------- //

# Início de remover_produto() --------------- //
def remover_produto():
  print('Bem-vindo ao menu de Remover Produtos')
  valor_desejado = int(input('Entre com o CÓDIGO do produto que deseja remover: '))
  for produto in lista_produto:
    if produto['codigo'] == valor_desejado:
      lista_produto.remove(produto)
      print('Produto Removido')

# Fim de remover_produto() --------------- //

# Início da Main --------------- //
print('Bem-vindo a Mercearia do Renan Protela Jorge')
while True:
  opcao_principal = input('Escolha a opção desejada: \n' +
                     '1 - Cadastrar Produto\n' + 
                     '2 - Consultar Produto\n' +
                     '3 - Remover Produto\n' +
                     '4 - Sair\n' +
                     '>> ')
  print()

  if opcao_principal == '1':
    codigo_produto += 1
    cadastrar_produto(codigo_produto)
  elif opcao_principal == '2':
    consultar_produto()
  elif opcao_principal == '3':
    remover_produto()
  elif opcao_principal == '4':
    break
  else:
    print('Opção Inválida. Tente Novamente...')
    continue
  
# Fim da Main --------------- //