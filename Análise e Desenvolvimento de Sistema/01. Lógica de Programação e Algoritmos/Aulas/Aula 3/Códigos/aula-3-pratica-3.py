# Exercícios: Condicionais Simples
idade, dano, escudo = 0
norte, sul, leste, oeste = False


# a)
if (idade > 60):
  print ('Você tem direito aos benefícios')

# b)
if (dano > 10 and escudo == 0):
  print ('Você está morto!')

# c)
if (norte or sul or leste or oeste):
  print ('Você escapou!')