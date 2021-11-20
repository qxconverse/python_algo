class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x_str = str(x)
        res_str = x_str[::-1]
        if neg == False:
            return int(res_str)
        else:
            return -int(res_str[0:len(res_str)-1])

    def isPalindrome(self, x: int) -> bool:
        # return str(x)[::-1] == str(x)
        if x < 0: return False
        ox = x
        y = 0
        while x != 0:
            y = y * 10 + (x % 10)
            x = int(x / 10)
            print(x)
            print(y)
        return ox == y

    def rob(self, nums) -> int:
        def dp(x):
            if x == 0:
                return 0
            if x == 1:
                return nums[0]
            return max(dp(x-1), nums[x-1] + dp(x-2))
        return dp(len(nums))

s = Solution()
# print(s.reverse(1534236469))

# print(s.isPalindrome(120))

print(s.rob([2,7,9,3,1]))