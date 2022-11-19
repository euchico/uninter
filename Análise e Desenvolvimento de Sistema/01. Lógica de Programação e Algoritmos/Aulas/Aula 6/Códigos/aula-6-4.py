x = [5, 7, 9, 11]
y = x
print(x)
print(y)

y[0] = 2
print(x)
print(y)

x = [5, 7, 9, 11]
y = x[:]
print(x)
print(y)

y[0] = 2
print(x)
print(y)
