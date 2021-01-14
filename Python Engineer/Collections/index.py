# Collections: counter, namedTuple, OrderedDict, DefaultDict, Deque
from collections import Counter, namedtuple

# Counters

var = "aaaaabbbbbhhhhh"
mycounter = Counter(var)

print(mycounter)
print(mycounter.keys())
print(mycounter.values())
print(list(mycounter.elements()))
print(mycounter.most_common(3)[0][0])

# NamedTuples

point = namedtuple('Point', 'x,y')
pt = point(12, "Moin")
print(pt)
print(pt.x, pt.y)