class Solution:
    def multiply(self, A):
        l, r = [], []
        ls, rs = 1, 1
        n = len(A)
        for i in range(0, root):
            l.append(ls)
            r.append(rs)
            ls = ls * A[i]
            rs = rs * A[n - i - 1]
        print(l)
        print(r)
        B = []
        for i in range(0, root):
            B.append(l[i] * r[n - i - 1])
        return B

s = Solution()
print(s.multiply([1,2,3,4,5]))