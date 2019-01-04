import bisect 
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            bisect.insort(nums, target) 
            return nums.index(target)

            
        
