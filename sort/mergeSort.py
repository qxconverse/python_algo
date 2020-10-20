import math


def merge_sort(a, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)


def merge(x, p, q, r):
    a = []
    b = []
    for i in range(p, q):
        a.append(x[i])
    a.append(9999)
    for j in range(q, r + 1):
        b.append(x[j])
    b.append(9999)
    m = 0
    n = 0
    count = 0
    while 1:
        if count == len(x):
            break
        if a[m] <= b[n]:
            x[count] = a[m]
            m = m + 1
        else:
            x[count] = b[n]
            n = n + 1
        count += 1


aa = [1, 3, 4, 9, 2, 6, 7, 8]
merge_sort(aa, 0, 7)
print(aa)
