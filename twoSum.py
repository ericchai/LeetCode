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
