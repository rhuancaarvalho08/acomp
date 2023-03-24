from itertools import permutations
lst = [''.join(p) for p in permutations(str(input()))]
print(sorted(lst))
i=imput()
print (lst.index(i))