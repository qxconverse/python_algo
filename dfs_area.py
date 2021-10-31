input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]

row = len(input)
col = len(input[0])
res = 0
max_res = 0


def cal_max_area():
    global max_res, res
    for i in range(0, row):
        for j in range(0, col):
            if input[i][j] == 1:
                dfs(i, j)
                # 每次递归完成后，进行一次比较
                max_res = max(res, max_res)
                # 并重置res
                res = 0
    return max_res

def dfs(i, j):
    '''
    1. 函数设计dfs(i, j)
    2. 终止条件
    i < 0 or i >= row or j < 0 or j >= col or input[i][j] == 0
    3. 递归的方向
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i-1, j)
    dfs(i+1, j)
    '''
    global res, max_res
    if i < 0 or i >= row or j < 0 or j >= col or input[i][j] == 0 or input[i][j] == -1:
        return
    res += 1
    # 为什么要置为-1？（为了标识改点已经遍历过了，防止无限循环遍历）
    # 以及它的影响？（没有影响，因为从连续区域里任何一点开始遍历，都会得到相同的结果，所以没必要再遍历了）
    input[i][j] = -1
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i-1, j)
    dfs(i+1, j)

print(cal_max_area())

