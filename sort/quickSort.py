def quick_sort(a, s, l):
    if s < l:
        m = partition(a, s, l)
        quick_sort(a, s, m - 1)
        quick_sort(a, m + 1, l)


def partition(a, s, l):
    mid = a[l]
    i = s - 1
    for j in range(s, l):
        if a[j] <= mid:
            i = i + 1
            swap(a, i, j)
    swap(a, i + 1, l)
    return i + 1


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


aa = [5, 7, 3, 2, 6, 8, 0, 1, 9, 4]
quick_sort(aa, 0, len(aa) - 1)

print(aa)
