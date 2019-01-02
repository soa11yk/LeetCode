class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]: #everytime only compares the value of the next index
                del nums[i] #del function removes the value from the said index
            else:
                i += 1
        return len(nums)
