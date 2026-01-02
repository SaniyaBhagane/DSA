# --------------------ARRAYS --------------------

# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

# Approach => In a loop keep count of 1s, then reset count when 0 is encountered. Keep track of max count in res variable. 

# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         count = 0
#         res = 0
#         for i in nums:
#             if i == 1:
#                 count += 1
#                 res = max(count, res)
#             else:
#                 count = 0
#         return res
# => The above approach can be optimized slightly by updating maxCount only when 0 is encountered.

# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         count = 0
#         maxCount = 0
#         for i in nums:
#             if i == 1:
#                 count += 1
#             else:
#                 maxCount = max(maxCount, count)
#                 count = 0
#         return max(maxCount, count)        
