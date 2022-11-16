def realce(s1):
  print('|', ('__' * 10), '|')
  print('|', ('__' * 10), '|')
  print (s1)
  print('|', ('__' * 10), '|')
  print('|', ('__' * 10), '|')

realce('           Zé')


def sub2(x, y):
  res = x - y
  print(res)

sub2(5, 7)
sub2(7, 5)
sub2(y = 7, x = 5)


def soma3(x = 0, y = 0, z = 0):
  res = x + y + z
  print(res)

soma3(1,2,3)
soma3(1,2)
soma3(1)
soma3()