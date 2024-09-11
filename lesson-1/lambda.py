a = [(1, 2), (5, 6), (7, 1), (2, 9)]
a.sort(key=lambda item: list(reversed(item)))

print(a)