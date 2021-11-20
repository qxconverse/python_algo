def kmp_find(pat, str):
    dp = kmp(pat)

    m = len(pat)
    n = len(str)
    j = 0

    for i in range(0, n):
        j = dp[j][ord(str[i])]
        if j == m:
            return i - m + 1
    return -1
    
    
def kmp(pat):
    m = len(pat)

    res = [[0 for i in range(0, 256)] for j in range(0, m)]
    res[0][ord(pat[0])] = 1
    X = 0

    for j in range(1, m):
        for c in range(0, 256):
            if c == ord(pat[j]):
                res[j][c] = j + 1
            else:
                res[j][c] = res[X][c]
        X = res[X][ord(pat[j])]

    return res    

pat = "aaab"

print(kmp_find(pat, "aaacaaab"))
print(kmp_find(pat, "aaaaaaab"))
