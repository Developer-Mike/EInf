import math

o = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
h = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def indexOf(arr: list[any], x: any) -> bool:
    lower = 0
    upper = len(arr) - 1
    current = 0
 
    while lower <= upper:
        current = (upper + lower) // 2
 
        if arr[current] < x:
            lower = current + 1
        elif arr[current] > x:
            upper = current - 1
        else: return current
 
    return -1

for l in (o, h):
    for i in range(-1, 13):
        assert indexOf(l, i) == (l.index(i) if i in l else -1)