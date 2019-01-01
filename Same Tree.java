/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// 3 cases apporach to this problem
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) return true; //if both p & q are null, return true
        if(p == null || q == null) return false; //if either or p & a is null, return false
        return (p.val == q.val) && isSameTree(p.left,q.left) && isSameTree(p.right,q.right);    
    }
}
