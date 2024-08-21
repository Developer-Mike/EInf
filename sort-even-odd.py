l = [3, 3, 2, 1, 6, 8]

def even_odd_sort(arr: list[int]):
    i_offset = 0
    for i in range(len(arr) - 1):
        if arr[i + i_offset]  % 2 != 0:
            arr.append(arr.pop(i + i_offset))
            i_offset -= 1

    return arr

print(even_odd_sort(l))