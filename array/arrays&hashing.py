# 1929: CONCATENATION OF ARRAY
# BRUTEFORCE: Using + Operator
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums + nums  # Concatenate the list with itself

# APPROACH 2: Using Loop and Append Method
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         result = []
#         for num in nums:
#             result.append(num)  # Add each element from nums
#         for num in nums:
#             result.append(num)  # Add each element again
#         return result

# APPROACH 3: Using Loop and Changing Element Value
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         result = [0] * (2 * n)  # Create a new list of size 2n
#         for i in range(n):
#             result[i] = nums[i]      # Copy the first part
#             result[i + n] = nums[i]  # Copy the second part
#         return result

# APPROACH 4: Using Extend Method
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         nums.extend(nums)  # Extend the list with itself
#         return nums

# APPROACH 5: Using * Operator
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums * 2  # Repeat the list twice


# -------------------------------------------------------------------------------------------------
# 217: CONTAINS DUPLICATES

# BRUTEFORCE APPROACH
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True
#         return False
    
# APPROACH 2 => USING SETS
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         num_set = set()

#         for n in nums:
#             if n in num_set:
#                 return True
#             num_set.add(n)
        
#         return False

# APPROACH 3 => USING SETS AND CONSIDERING LENGTH
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return True if len(set(nums)) < len(nums) else False


# -------------------------------------------------------------------------------------------------
# 242: VALID ANAGRAM


# -------------------------------------------------------------------------------------------------
