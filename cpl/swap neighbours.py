def swap_neighbors(a: list):
    for i in range(0, len(a) - 1, 2):
        a[i], a[i + 1] = a[i + 1], a[i]
L= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
swap_neighbors(L)
print(L)
