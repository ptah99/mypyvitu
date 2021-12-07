# sets: unordered, mutable, no duplicate
myset = {1, 2, 3}
print(myset)
set = set()
set.add(1)
set.add(2)

print(set)
# unions
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setC = {1, 2, 3}
diff = setA.difference(setB)
print(diff)
dif = setA.symmetric_difference(setB)
print(dif)
setA.update(setB)
print(setA)
print(setC.issubset(setA))
print(setB.issuperset(setC))
