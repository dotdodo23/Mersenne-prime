def isMersennePrime(p):
  s = 4
  M = 2 ** p - 1
  for i in range(p-2):
    s = (s ** 2 - 2) % M
  if s == 0:
    return True
  else:
    return False
