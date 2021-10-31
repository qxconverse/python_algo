class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        rec = [-1] * 58
        for i in range(len(s)):
            index = ord(s[i]) - ord('A')
            if rec[index] == -1:
                rec[index] = i
            else:
                rec[index] = -2
        min_index = 999999
        for i in rec:
            if i >= 0 and i < min_index:
                min_index = i
        if min_index == 9999: 
            return -1
        return min_index

s = Solution()
print(s.FirstNotRepeatingChar("aa"))
