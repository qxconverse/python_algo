# -*- coding:utf-8 -*-
import functools

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        numbers_str = list(map(str, numbers))
        # 注意一定是>0和<0
        compare_func = lambda x, y: 1 if x + y > y + x else -1
        numbers_str.sort(key=functools.cmp_to_key(compare_func))
        return ''.join(numbers_str)

s = Solution()
print(s.PrintMinNumber([3,32,321]))