g = int(input())
degree = 0

def soma_g(g):
  return sum(int(d) for d in str(g))

while g > 9:
  g = soma_g(g)
  degree = degree + 1

print(degree)
print(g)

if g != 9:
   print(False)
else:
   print(True)