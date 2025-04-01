from itertools import permutations

name = input("Type a name, but try to keep it short: ")
perms = [''.join(i) for i in permutations(name)]
print(perms)
print(*perms, sep='\n')
print(len(perms))