cadastro = {'nome': [], 'sexo':[], 'ano':[]}

while True:
  terminar = input('Deseja cadastrar uma pessoa [S/N]? ')
  if (terminar.upper() in 'N'):
    break
  if (terminar.upper() not in 'S'):
    print('Digite S para SIM ou N para Não')
    continue

  nome = input('Qual o seu nome? ')
  sexo = input('Qual seu sexo [M/F]? ')
  ano = input('Qual seu ano de nascimento? ')
  cadastro['nome'].append(nome)
  cadastro['sexo'].append(sexo.upper())
  cadastro['ano'].append(ano)

print(cadastro)