mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print('Tupla: ', mochila)

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)

mochila[2] = 'Laranja'
print('Lista: ', mochila)

mochila.append('Ovos')
print('Lista: ', mochila)

mochila.insert(1, 'Canivete')
print('Lista: ', mochila)

del mochila[1]
print('Lista: ', mochila)

mochila.remove('Ovos')
print('Lista: ', mochila)
