# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def mps(root):
            if root is None:
                return (0, float("-inf"))
            lsb, lrmps = mps(root.left)
            rsb, rrmps = mps(root.right)
            max_child_branch_sum = max(lsb,rsb)
            max_sum_as_branch = max(max_child_branch_sum + root.val, root.val)
            max_ps_as_traingle = max(max_sum_as_branch, lsb + root.val + rsb)
            rmps = max(lrmps, rrmps, max_ps_as_traingle)
            return(max_sum_as_branch, rmps)

        _, max_path_sum = mps(root)
        return max_path_sum