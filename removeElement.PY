class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            element = nums[i]
            
            if element == val:
                del nums [i]
                n = n - 1
            else:
