# --------------------ARRAYS --------------------

# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

# Approach
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for i in nums:
            if i == 1:
                count += 1
                res = max(count, res)
            else:
                count = 0
        return res
        
