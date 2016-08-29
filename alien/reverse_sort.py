from itertools import cycle
from random import shuffle
def reverse_sort(strings):
    letters = list(set([a for a in reduce(lambda a, b: a + b, strings)]))
    stopped = False
    while True:
        stopped = False
        for s in strings:
            for c1, c2 in zip(s, s[1::]):
                if letters.index(c2) < letters.index(c1):
                    stopped = True
                    letters.pop(letters.index(c2))
                    letters.insert(letters.index(c1) + 1, c2)
        if not stopped:
            break
    return letters
