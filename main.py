def factor_pairs(x):
  ls = []
  i = 1
  while i * i <= abs(x):
    if abs(x) % i == 0:
      ls.append((-i, -x // i))
      ls.append((i, x // i))
    i += 1
  return ls
  
for a,b in factor_pairs(-42):
  print(a * b)
