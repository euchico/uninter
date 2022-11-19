print ('Bem vindo a loja do Francisco de Paula Neto')

valorProduto = float(input('Entre com o valor do produto: '))
qdtProduto = int(input('Entre com a quantidade: '))
subtotal = valorProduto * qdtProduto

if (subtotal < 200):
  valorFinal = subtotal
elif (200 <= subtotal < 400):
  valorFinal = subtotal - (subtotal * 0.04)
elif (400 <= subtotal < 700):
  valorFinal = subtotal - (subtotal * 0.07)
else:
  valorFinal = subtotal - (subtotal * 0.10)

print('O valor sem desconto: {}'.format(subtotal))
print('O valor sem desconto: {}'.format(valorFinal))