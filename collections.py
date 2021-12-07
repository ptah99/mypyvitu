# collections: counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

# counter is a dictionary subclass for counting hashable objects
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.values())  # .keys, .items
print(my_counter.most_common(1))  # access element (1)[0][0]
print(list(my_counter.elements()))

# namedtuple
from collections import namedtuple

point = namedtuple('point', 'x,y')
pt = point(1, -4)
print(pt.x, pt.y)

# OrderedDict
from collections import OrderedDict

# python 3.7 makes this less useful bcoz it also remembers the order
ordered_dict = OrderedDict()  # or {} works
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

# defaultdict; default value is key id not set yet
from collections import defaultdict
