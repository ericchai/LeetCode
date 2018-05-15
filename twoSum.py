# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """              
        for j,num in enumerate(nums):
            for k,second_num in enumerate(nums[j+1:]):
                if num+second_num == target:
                    return list((j,k+j+1))
        return False
    
    
    
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。    
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return x >= 0 and str(x)[::1] == str(x)[::-1]
