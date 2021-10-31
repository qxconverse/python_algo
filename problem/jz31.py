# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # def sumOf1(k):
        #     sum = 0
        #     while k > 0:
        #         sum += (1 if k % 10 == 1 else 0)
        #         k = int(k / 10)
        #     return sum
        
        # f = 0
        # for i in range(1, n + 1):
        #     f += sumOf1(i)
        # return f

        origin = n
        total = 0
        k = 1
        while n > 0:
            # 首先加上固定的部分
            total += origin // (k * 10) * k
            # 待比较的数字，为超出
            to_cmp_num = origin % (k * 10)
            # 和基数对比，大于基数，就要加额外的部分，额外的部分取它和基数的差值，但最大为基数k
            if to_cmp_num >= k:
                total += min(to_cmp_num - k + 1, k)
            n = int(n / 10)
            k *= 10
        return total
    
s = Solution()
print(s.NumberOf1Between1AndN_Solution(328))
