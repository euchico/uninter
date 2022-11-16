def comida():
  ovos = 'Variável local de comida'
  print(ovos)

def bacon():
  ovos = 'Variável local de bacon'
  print(ovos)
  comida()
  print(ovos)

ovos = 'Variável global'
bacon()
print(ovos)