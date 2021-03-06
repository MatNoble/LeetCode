#==================================================
#==>      Title: find-the-duplicate-number                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/14/2021
#==================================================

"""
https://leetcode-cn.com/problems/find-the-duplicate-number/
"""

class Solution:
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        find = 0
        while True:
            find = nums[find]
            slow = nums[slow]
            if slow == find:
                break
        return slow

nums = [2, 3, 1, 5, 1, 4]
mat = Solution()
mat.findDuplicate(nums)
