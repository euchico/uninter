mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0])

print(mochila[0][0])
print(mochila[2][1])

for item in mochila:
  for letra in item:
    print(letra, end='')
  print()

for i in range(0, len(mochila)):
  for j in range(0, len(mochila[i])):
    print(mochila[i][j], end='')
  print()