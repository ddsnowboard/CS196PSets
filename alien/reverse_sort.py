from itertools import cycle
def reverse_sort(strings):
    letters = {a: None for a in reduce(lambda a, b: a + b, strings)}
