from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                move = nums[i-1] - nums[i] + 1
                nums[i] += move
                res += move
        return res


s = Solution()
print(s.minIncrementForUnique([3,2,1,2,1,7]))