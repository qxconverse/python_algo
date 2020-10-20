def select_sort(a):
    for i in range(0, len(a)):
        min_l = i
        for j in range(i, len(a)):
            if a[j] < a[min_l]:
                min_l = j
        temp = a[i]
        a[i] = a[min_l]
        a[min_l] = temp


aa = [5, 7, 3, 2, 6, 8, 0, 1, 9, 4, 54, 6, 67, 67, 88, 98, 9, 0, 5, 352]
select_sort(aa)
print(aa)
