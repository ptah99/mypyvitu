# itertools : product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
import operator
from itertools import groupby
from itertools import count, cycle, repeat

# product:
a = [1, 2]
b = [3, 4]
prod = product(a, b)  # , repeat=2
print(list(prod))

# permutations: return all possible ordering of inputs

a = [1, 2, 3]
p = permutations(a)
c = permutations(a, 2)
print(list(p))
print(list(c))

# combinations: all possible combination
# if repetition needed import combinations_with_replacement

f = [1, 2, 3, 4]
cb = combinations(f, 2)
print(list(cb))
comb_wtr = combinations_with_replacement(f, 2)
print(list(comb_wtr))

# accumulate: makes iterator that returns accumulated sums on input
# operator helps in other functions like multiplication, max,,,
ac = [1, 2, 5, 3, 4, ]
acc = accumulate(ac, func=operator.mul)
acm = accumulate(ac, func=max)  # max at the position starting with index 0
print(ac)
print(list(acc))
print(list(acm))

# groupby: makes a return key from iterables

g = [1, 2, 3, 4]
grb = groupby(g, key=lambda x: x < 3) # lambda replaces need for a function
for key, value in grb:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Ben', 'age': 25},
           {'name': 'Lisa', 'age': 30}, {'name': 'Claire', 'age': 30}]
grp = groupby(persons, key=lambda x: x['age'])
for key, value in grp:
    print(key, list(value))

# infinite iterators

for i in count(10):
    print(i)
    if i == 15:
        break

n = [1, 2, 3]
# for i in cycle(n):
#     print(i)

for i in repeat(n, 4):
    print(i)
