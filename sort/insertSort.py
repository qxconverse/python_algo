def insert_sort(a):
    for i in range(1, len(a)):
        m = a[i]
        for j in range(i - 1, -1, -1):
            if m >= a[j]:
                break
            a[j + 1] = a[j]
            a[j] = m


aa = [5, 7, 3, 2, 6, 8, 0, 1, 9, 4]
insert_sort(aa)
print(aa)
