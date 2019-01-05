class Solution:
    def constructMaximumBinaryTree (self, nums):
        def maxTree (nums):
            i = nums.index (max(nums)) #to find the index of maximum
            node = TreeNode (nums[i]) #create the tree and set the root
            if len(nums[i+1:]) > 0:
                   node.right = maxTree(nums[i+1:])
            if len(nums[:i]) > 0:
                   node.left = maxTree(nums[:i])
            return node
        return maxTree (nums)
             
