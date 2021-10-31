# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, root):
        # write code here
        if root == 0:
            return 0
        if root == 1:
            return 1
        a0 = 0
        a1 = 1
        for i in range(2, root + 1):
            b = a0 + a1
            a0 = a1
            a1 = b
        return a1

s = Solution()
print(s.Fibonacci(9))
