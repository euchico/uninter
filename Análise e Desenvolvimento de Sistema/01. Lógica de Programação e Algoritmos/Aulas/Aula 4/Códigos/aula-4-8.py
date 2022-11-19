while True:
  nome = input('Qual o seu nome? ')
  if (nome != 'teste'):
    continue
  
  senha = input('Qual a sua senha? ')
  if (senha == '123456'):
    break

print('Acesso concedido.')