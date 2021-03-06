#==================================================
#==>      Title: valid-parentheses
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/15/2021
#==================================================

"""
stack
https://leetcode-cn.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s):
        dict = {'(':1, ')':-1, '{':2, '}':-2, '[':3, ']':-3}
        stack = []
        for val in s:
            temp = dict[val]
            if len(stack) != 0 and stack[-1] > 0 and stack[-1] + temp == 0:
                stack.pop()
            else:
                stack.append(temp)
        return True if len(stack) == 0 else False

s = "()[]{)"
s = ")("
s = "()"
s = "([}}])"
mat = Solution()
mat.isValid(s)
