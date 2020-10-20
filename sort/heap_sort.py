def heap_adjust(l, parent, length):
    temp = l[parent]
    child = 2 * parent + 1

    while child < length:
        if child + 1 < length and l[child] < l[child + 1]:
            child += 1
        if l[child] <= temp:
            break
        l[parent] = l[child]
        parent = child
        child = parent * 2 + 1
    l[parent] = temp


def head_sort(l):
    length = len(l)
    # 创建初始堆，从第一个非叶子节点开始，下标为length / 2，一直比较到下标为0的数
    for i in range(length // 2, -1, -1):
        heap_adjust(l, i, length)

    # 从length-1到1，第0个元素就不用考虑了
    for i in range(length - 1, 0, -1):
        l[0], l[i] = l[i], l[0]
        heap_adjust(l, 0, i)

        print("The " + str(length - i) + " time")
        print(l)
    return l


if __name__ == '__main__':
    ls = [2, 6, 3, 5, 8, 4, 1, 7]
    a = head_sort(ls)
    print(a)
