# Exercícios 1 

preco = float(input('Informe o preço(R$) do produto: '))
porcentagemDesconto = float(input('Informe o desconto(%) do produto: '))

valorDesconto = ((preco * porcentagemDesconto) / 100)

print('O valor do desconto dado será de {}'.format(valorDesconto))
print('O preço final do produto será de {}'.format(preco - valorDesconto))
