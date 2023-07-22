# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 0
        def dfs(root):
            if root is None:
                return 0
            leftMax = dfs(root.left)
            rightMax= dfs(root.right)
            leftMax = leftMax + 1 if root.left and root.left.val == root.val else 0
            rightMax = rightMax + 1 if root.right and root.right.val == root.val else 0
                
            self.maxLen = max(self.maxLen, leftMax+rightMax)
            return max(leftMax, rightMax)
        dfs(root)
        return self.maxLen
        