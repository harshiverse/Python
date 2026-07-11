#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#You must solve this problem without using the library's sort function.

#Example 1:
#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]
#Example 2:

#Input: nums = [2,0,1]
#Output: [0,1,2]

#Constraints:

#n == nums.length
#1 <= n <= 300
#nums[i] is either 0, 1, or 2.
 

#Follow up: Could you come up with a one-pass algorithm using only constant extra space?


#----------------Counting Sort (frequency counting) approach----------------

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        count_zero = 0
        count_one = 0
        count_two = 0

        for i in nums:
            if i == 0:
               count_zero = count_zero + 1

            elif i == 1:
                count_one = count_one + 1

            else:
                count_two += 1        
        j=0
        while count_zero > 0:
              nums [j] = 0
              j += 1
              count_zero -= 1

        while count_one > 0:
              nums [j] = 1
              j += 1
              count_one -=1

        while count_two > 0:
              nums [j] = 2
              j += 1
              count_two -= 1      

# This is a valid solution. It passes all the test cases. It is still not the optimal solution because it use 2 PASSES.
# First pass: Count the number of 0s, 1s, and 2s.
# Second pass: Rewrite the array.
# Time Complexity: O(n);  Space Complexity: O(1)

#------------- Optimal Solution: Dutch National Flag (DNF) Approach ---------

# This is a form of three-pointer. This is the famous one-pass solution.

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        n = len(nums)
        low = 0
        mid = 0
        high = n-1

        while mid <= high:

            if nums[mid] == 0:
               nums[mid], nums[low] = nums[low], nums[mid]      #tuple unpacking or multiple assignment
               low += 1
               mid += 1

            elif  nums[mid] == 1:
               mid += 1

            else:
                nums[low], nums[high] = nums[high], nums[low]
                high -= 1

