weight = [4, 54, 1, 5, 22, 18, 32, 15]
values = [3, 3, 11, 23, 20, 9, 14, 33]

solution = [0] * 8
ans = []
max_weight, max_value = 100, 0


def back_trace(n, cur_w, cur_v):
    global max_value
    global ans

    if cur_w > max_weight:
        return

    if n == 8:
        if cur_v > max_value:
            max_value = cur_v
            ans = [i for i in solution]
        return

    # 放进背包
    solution[n] = 1
    back_trace(n + 1, cur_w + weight[n], cur_v + values[n])

    # 不放进背包
    solution[n] = 0
    back_trace(n + 1, cur_w, cur_v)


if __name__ == '__main__':
    back_trace(0, 0, 0)
    print(ans)
    print(max_value)
